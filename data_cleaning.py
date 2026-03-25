def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    # OR USE
    cleaned= []
    removed_val = []
    for item in data:
        if item.isdigit():
            cleaned.append(int(item))
        else:
            removed_val.append(item)

        
    return (cleaned,removed_val)