import requests
import json
import re
import sys
from bs4 import BeautifulSoup
from configs.settings import BASE_API_URL
from parsers.team_parser import parse_team
from db.mysql import insert_team, insert_competition
from utils.helpers import logger, smart_delay
from pprint import pprint



def crawl_team_url():
    url = "https://www.efootballdb.com/teams"
    resp = requests.get(url)
    if resp.status_code == 200:
        html = resp.text
        # Lưu HTML vào file để kiểm tra
        data = parse_competitions_and_teams(html)
        print(f"✅ Đã tải thành công {len(data)} giải đấu và đội bóng từ {url}")


    else:
        print(f"❌ Lỗi khi tải trang: {resp.status_code}")


def parse_competitions_and_teams(html: str):
    soup = BeautifulSoup(html, "html.parser")
    result = []

    # Tìm block chứa danh sách giải đấu (cột bên trái)
    competition_blocks = soup.select('div.col-12.col-xl-3 div[data-bs-toggle="collapse"]')

    for comp_div in competition_blocks:
        comp_id = comp_div.get("aria-controls", "").replace("teams-id-", "")
        if not comp_id:
            continue

        name_span = comp_div.select_one("span")
        img_tag = comp_div.select_one("img")


        logo_path = img_tag["src"] if img_tag else ""
        logger(f"[DEBUG] logo_path HTML: {logo_path}")

        

        competition = {
            "com_id": int(comp_id),
            "name": name_span.get_text(strip=True) if name_span else "",
            "logo_path": logo_path,
        }

        # Insert competition vào DB
        insert_competition(competition)

        # Gọi API chi tiết cho từng team tương ứng
        team_div = soup.select_one(f'div#teams-id-{comp_id}')
        if team_div:
            for team_el in team_div.select("div.team-button"):
                a_tag = team_el.select_one("a")
                if not a_tag or "href" not in a_tag.attrs:
                    continue
                match = re.search(r'id=(\d+)', a_tag["href"])
                if not match:
                    continue

                team_id = int(match.group(1))
                raw = get_team_detail(team_id)
                if raw:
                    parsed = parse_team(raw, competition_id=int(comp_id))

                    insert_team(parsed)
                    smart_delay()

        result.append(competition)

    # Ghi ra file JSON để debug
    with open("competitions.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    return result



def get_team_detail(team_id):
    url = f"{BASE_API_URL}/teams/{team_id}"
    resp = requests.get(url)
    print(f"URL: {url}")

    if resp.status_code == 200:
        return resp.json()
    else:
        logger(f"❌ Failed to get team {team_id}, status: {resp.status_code}")
        return None

def crawl_team():
    sample_id = 108
    raw = get_team_detail(sample_id)
    #set raw id = sample_id
    raw["data"]["id"] = sample_id
    if raw:
        team = parse_team(raw)
        insert_team(team)

if __name__ == "__main__":
    crawl_team_url()