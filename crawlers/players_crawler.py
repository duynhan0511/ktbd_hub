import requests
from parsers.player_parser import parse_player
from db.mysql import insert_player
from configs.settings import BASE_API_URL
from utils.helpers import logger, smart_delay

# def get_player_detail(player_id):
#     url = f"{BASE_API_URL}/players/{player_id}"
#     resp = requests.get(url)
#     if resp.status_code == 200:
#         return resp.json()
#     else:
#         logger(f"❌ Failed to get player {player_id}, status: {resp.status_code}")
#         return None

def crawl_players():
    sample_id = "52780584775806"
    raw = get_player_detail(sample_id)
    if raw:
        player = parse_player(raw)
        insert_player(player)

def get_players_list(page):
    url = f"{BASE_API_URL}/players?page={page}"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            logger(f"❌ Lỗi lấy danh sách cầu thủ trang {page}: {resp.status_code}")
    except Exception as e:
        logger(f"❌ Exception tại page {page}: {e}")
    return None

def get_player_detail(player_id):
    url = f"{BASE_API_URL}/players/{player_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None

def crawl_players_all():
    page = 1
    logger("🚀 Bắt đầu crawl danh sách cầu thủ...")

    first_page = get_players_list(page)
    if not first_page:
        logger("❌ Không thể lấy được trang đầu tiên.")
        return

    last_page = first_page.get("meta", {}).get("last_page", 1)
    logger(f"📖 Tổng số trang: {last_page}")

    while page <= last_page:
        logger(f"📦 Đang xử lý trang {page}...")
        result = get_players_list(page)
        if not result:
            logger(f"⚠️ Bỏ qua trang {page}")
            page += 1
            continue


        if page == 3:
            logger(f"❌ Đã đến trang 3, dừng lại.")
            break

        for p in result.get("data", []):
            pes_id = p.get("pes_id")
            if not pes_id:
                continue
            detail = get_player_detail(pes_id)
            if detail:
                parsed = parse_player(detail)
                insert_player(parsed)
            smart_delay()

        page += 1
    logger("🎉 Hoàn tất crawl danh sách cầu thủ.")

if __name__ == "__main__":
    crawl_players_all()