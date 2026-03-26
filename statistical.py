import statistics as stats
import math 
import matplotlib.pyplot as plt

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
    

def variance(data: list) -> float:
    # add_numbers = 0
    # for num in data:
    #     add_numbers += num
    
    # average_num = add_numbers/len(data)

    # var_sum = 0
    # for point in data:
    #     var_sum += math.pow((point-average_num),2)
    
    # sam_var= var_sum / (len(data) - 1)

    sam_var = stats.variance(data)
    
    return sam_var

def standard_dev(data:list) -> float:
    # std = math.sqrt(variance(data))

    std = stats.stdev(data)

    return std

def line_chart(data:list) -> float:
    fig, ax = plt.subplots(figsize = (6,5))
    ax.plot(data)

    return plt.show()
