import statistics as stats

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    # add_numbers = 0
    # for num in data:
    #     add_numbers += num
    
    # average_num = add_numbers/len(data)

    average_num = stats.mean(data)

    return average_num

def median(data: list) -> float:
    """
    """
    # sorted_data = sorted(data)
    
    # if len(sorted_data) % 2 == 0:
    #     median_value = (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2
    # else:
    #     median_value = sorted_data[len(sorted_data) // 2]
    median_value = stats.median(data)

    return median_value

def range(data: list) -> float:
    """
    """
    range_value = max(data) - min(data)
    

    return range_value


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass

def variance(data: list) -> float:
    pass