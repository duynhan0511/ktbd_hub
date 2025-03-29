import requests
import time
from configs.settings import BASE_API_URL
from parsers.manager_parser import parse_manager
from db.mysql import insert_manager
from utils.helpers import logger

def get_manager_detail(manager_id):
    url = f"{BASE_API_URL}/managers/{manager_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        logger(f"❌ Failed to get manager {manager_id}, status: {resp.status_code}")
        return None

def get_managers_list(page: int):
    url = f"{BASE_API_URL}/managers?page={page}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json().get("data", [])
    else:
        logger(f"❌ Failed to fetch manager list page {page}, status: {resp.status_code}")
        return []
    
def crawl_managers_all():
    page = 1
    total_inserted = 0

    while True:
        logger(f"📦 Crawling page {page}...")
        url = f"{BASE_API_URL}/managers?page={page}"
        resp = requests.get(url)
        if resp.status_code != 200:
            logger(f"❌ Failed to fetch page {page}, status: {resp.status_code}")
            break

        json_data = resp.json()
        managers = json_data.get("data", [])
        last_page = json_data.get("meta", {}).get("last_page", page)

        if page == 3:
            logger(f"❌ Đã đến trang 3, dừng lại.")
            break

        if not managers:
            logger(f"✅ Hết dữ liệu ở trang {page}, kết thúc.")
            break

        for m in managers:


            parsed = parse_manager(m)  # parse trực tiếp từ item của list
            insert_manager(parsed)
            total_inserted += 1
            time.sleep(0.8)  # delay để tránh bị block

        if page >= last_page:
            logger("✅ Đã đến trang cuối cùng, dừng lại.")
            break
        page += 1

    logger(f"🎉 Tổng cộng đã crawl {total_inserted} managers.")


def crawl_managers_test():
    sample_id = "17595138936066"
    raw = get_manager_detail(sample_id)
    if raw:
        manager = parse_manager(raw)
        insert_manager(manager)

if __name__ == "__main__":
    crawl_managers_all()