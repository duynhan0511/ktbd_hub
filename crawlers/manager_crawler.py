import requests
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

def crawl_managers():
    sample_id = "17595138936066"
    raw = get_manager_detail(sample_id)
    if raw:
        manager = parse_manager(raw)
        insert_manager(manager)

if __name__ == "__main__":
    crawl_managers()