def parse_team(raw):
    data = raw.get("data", {})

    return {
        "team_id": data.get("id"),
        "manager_id": data.get("manager_id"),
        "base_manager_id": data.get("base_manager_id"),
        # "base_manager_id": data.get("base_manager_id"),
        "transfer_budget": data.get("transfer_budget"),
        "salary_budget": data.get("salary_budget"),
        "name": data.get("english_name"),
        "official_name": data.get("english_name"),
        "short_name": data.get("licensed_abb_name"),
        "region_id": "",
        "stadium_id": data.get("stadium_id"),
        "team_sort_number": data.get("team_sort_number"),
        "non_playable_league": data.get("non_playable_league"),
    }