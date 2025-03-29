import requests
from configs.settings import BASE_API_URL
from parsers.team_parser import parse_team
from db.mysql import insert_team
from utils.helpers import logger

def get_team_detail(team_id):
    url = f"{BASE_API_URL}/teams/{team_id}"
    resp = requests.get(url)
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
    crawl_team()