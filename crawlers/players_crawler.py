import requests
from parsers.player_parser import parse_player
from db.mysql import insert_player
from configs.settings import BASE_API_URL
from utils.helpers import logger

def get_player_detail(player_id):
    url = f"{BASE_API_URL}/players/{player_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        logger(f"❌ Failed to get player {player_id}, status: {resp.status_code}")
        return None

def crawl_players():
    sample_id = "52780584775806"
    raw = get_player_detail(sample_id)
    if raw:
        player = parse_player(raw)
        insert_player(player)

if __name__ == "__main__":
    crawl_players()