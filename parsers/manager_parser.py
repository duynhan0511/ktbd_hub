def parse_manager(raw):
    # data = raw.get("data", {})
    data = raw
    country = data.get("country", {})
    booster = data.get("booster", {})

    return {
        "pes_id": data.get("pes_id"),
        "base_pes_id": data.get("base_pes_id"),
        "manager_name": data.get("english_name"),
        "reputation": data.get("reputation"),
        "age": data.get("age"),
        "nationality_id": country.get("pes_id"),
        "is_boosted": 1 if booster else 0,
        "boost_skill_type": booster.get("attribute_value") if booster else None,
        "possession_game": data.get("possession_game"),
        "quick_counter": data.get("quick_counter"),
        "long_ball_counter": data.get("long_ball_counter"),
        "out_wide": data.get("out_wide"),
        "long_ball": data.get("long_ball"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at")
    }