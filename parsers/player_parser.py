def parse_player(raw):
    data = raw.get("data", {})

    return {
        "pes_id": data.get("pes_id"),
        "base_pes_id": data.get("base_pes_id"),
        "variation": data.get("variation"),

        "player_name": data.get("player_name"),
        "shirt_name": data.get("shirt_name"),
        "version_title": data.get("card_name"),  # ví dụ: 'POTW International Cup 1 Dec 22'
        "card_type": data.get("card_type"),       # featured, epic, legendary, ...
        "image_url": data.get("player_img_url"),

        "nationality_id": data.get("nationality_id"),
        "current_team_id": data.get("team_id"),
        "age": data.get("age"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "strong_foot": data.get("strong_foot"),
        "weekly_form": data.get("weekly_form"),
        "injury_resistance": data.get("injury_resistance"),
        "main_position": data.get("main_position"),

        "max_level": data.get("max_level"),
        "price": data.get("price"),
        "market_value": data.get("market_value"),

        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at")
    }