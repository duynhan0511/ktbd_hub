import pymysql
import hashlib
import json
from configs.settings import MYSQL_CONFIG
from utils.helpers import logger
import traceback

def generate_hash(data: dict) -> str:
    data_clean = {k.strip(): v for k, v in data.items() if k not in ("created_at", "updated_at")}
    return hashlib.sha256(json.dumps(data_clean, sort_keys=True).encode()).hexdigest()

def insert_player(player):
    player_hash = generate_hash(player)
    player["data_hash"] = player_hash
    conn = pymysql.connect(**MYSQL_CONFIG) 
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT data_hash FROM players WHERE pes_id = %s", (player["pes_id"],))
            result = cursor.fetchone()

            print("result", result)

            if result is not None and result["data_hash"] == player_hash:
                logger(f"⏩ Player {player['player_name']} ({player['pes_id']}) không thay đổi, bỏ qua.")
                return

            sql = """
            INSERT INTO players (
                pes_id, base_pes_id, variation,
                player_name, shirt_name, version_title, card_type, image_url,
                nationality_id, current_team_id, age, height, weight,
                strong_foot, weekly_form, injury_resistance, main_position,
                max_level, price, market_value, data_hash
            ) VALUES (
                %(pes_id)s, %(base_pes_id)s, %(variation)s,
                %(player_name)s, %(shirt_name)s, %(version_title)s, %(card_type)s, %(image_url)s,
                %(nationality_id)s, %(current_team_id)s, %(age)s, %(height)s, %(weight)s,
                %(strong_foot)s, %(weekly_form)s, %(injury_resistance)s, %(main_position)s,
                %(max_level)s, %(price)s, %(market_value)s, %(data_hash)s
            )
            ON DUPLICATE KEY UPDATE
                player_name = VALUES(player_name),
                shirt_name = VALUES(shirt_name),
                version_title = VALUES(version_title),
                card_type = VALUES(card_type),
                image_url = VALUES(image_url),
                nationality_id = VALUES(nationality_id),
                current_team_id = VALUES(current_team_id),
                age = VALUES(age),
                height = VALUES(height),
                weight = VALUES(weight),
                strong_foot = VALUES(strong_foot),
                weekly_form = VALUES(weekly_form),
                injury_resistance = VALUES(injury_resistance),
                main_position = VALUES(main_position),
                max_level = VALUES(max_level),
                price = VALUES(price),
                market_value = VALUES(market_value),
                data_hash = VALUES(data_hash),
                updated_at = CURRENT_TIMESTAMP;
            """
            cursor.execute(sql, player)
        conn.commit()
        logger(f"✅ Đã insert player {player['player_name']} ({player['pes_id']}) vào MySQL")
    except Exception as e:
        print("⚠️ Lỗi thật:", e)
        print("⚠️ Dữ liệu player:", player)
        traceback.print_exc()
    finally:
        conn.close()

def insert_manager(manager):
    manager_hash = generate_hash(manager)
    manager["data_hash"] = manager_hash
    conn = pymysql.connect(**MYSQL_CONFIG)
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT data_hash FROM managers WHERE pes_id = %s", (manager["pes_id"],))
            result = cursor.fetchone()
            if result is not None and result["data_hash"] == manager_hash:
                logger(f"⏩ Manager {manager['manager_name']} ({manager['pes_id']}) không thay đổi, bỏ qua.")
                return

            sql = """
            INSERT INTO managers (
                pes_id, base_pes_id, manager_name, reputation, age,
                nationality_id, boost_skill_type, is_boosted,
                possession_game, quick_counter, long_ball_counter,
                out_wide, long_ball, data_hash
            ) VALUES (
                %(pes_id)s, %(base_pes_id)s, %(manager_name)s, %(reputation)s, %(age)s,
                %(nationality_id)s, %(boost_skill_type)s, %(is_boosted)s,
                %(possession_game)s, %(quick_counter)s, %(long_ball_counter)s,
                %(out_wide)s, %(long_ball)s, %(data_hash)s
            )
            ON DUPLICATE KEY UPDATE
                manager_name = VALUES(manager_name),
                reputation = VALUES(reputation),
                age = VALUES(age),
                nationality_id = VALUES(nationality_id),
                boost_skill_type = VALUES(boost_skill_type),
                is_boosted = VALUES(is_boosted),
                possession_game = VALUES(possession_game),
                quick_counter = VALUES(quick_counter),
                long_ball_counter = VALUES(long_ball_counter),
                out_wide = VALUES(out_wide),
                long_ball = VALUES(long_ball),
                data_hash = VALUES(data_hash),
                updated_at = CURRENT_TIMESTAMP;
            """
            cursor.execute(sql, manager)
        conn.commit()
        logger(f"✅ Đã insert manager {manager['manager_name']} ({manager['pes_id']}) vào MySQL")
    except Exception as e:
        print("❌ Lỗi insert manager:", e)
        traceback.print_exc()
    finally:
        conn.close()

def insert_team(team):
    team_hash = generate_hash(team)
    team["data_hash"] = team_hash
    conn = pymysql.connect(**MYSQL_CONFIG)
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT data_hash FROM teams WHERE team_id = %s", (team["team_id"],))
            result = cursor.fetchone()
            if result is not None and result["data_hash"] == team_hash:
                logger(f"⏩ Team {team['name']} (#{team['team_id']}) không thay đổi, bỏ qua.")
                return

            sql = """
            INSERT INTO teams (
                team_id, manager_id, base_manager_id,
                transfer_budget, salary_budget, name, official_name, short_name,
                region_id, stadium_id, team_sort_number, non_playable_league, data_hash
            ) VALUES (
                %(team_id)s, %(manager_id)s, %(base_manager_id)s,
                %(transfer_budget)s, %(salary_budget)s, %(name)s, %(official_name)s, %(short_name)s,
                %(region_id)s, %(stadium_id)s, %(team_sort_number)s, %(non_playable_league)s, %(data_hash)s
            )
            ON DUPLICATE KEY UPDATE
                manager_id = VALUES(manager_id),
                base_manager_id = VALUES(base_manager_id),
                transfer_budget = VALUES(transfer_budget),
                salary_budget = VALUES(salary_budget),
                name = VALUES(name),
                official_name = VALUES(official_name),
                short_name = VALUES(short_name),
                region_id = VALUES(region_id),
                stadium_id = VALUES(stadium_id),
                team_sort_number = VALUES(team_sort_number),
                non_playable_league = VALUES(non_playable_league),
                data_hash = VALUES(data_hash),
                updated_at = CURRENT_TIMESTAMP;
            """
            cursor.execute(sql, team)
        conn.commit()
        logger(f"✅ Đã insert team {team['name']} (#{team['team_id']}) vào MySQL")
    except Exception as e:
        print("⚠️ Lỗi thật:", e)
        print("⚠️ Dữ liệu team:", team)
        traceback.print_exc()
    finally:
        conn.close()
