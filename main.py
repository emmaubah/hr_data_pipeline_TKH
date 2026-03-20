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


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    add_numbers = 0
    for num in data:
        add_numbers += num
    
    average_num = add_numbers/len(data)

    return average_num



def median(data: list) -> float:
    """
    """
    sorted_data = sorted(data)
    
    if len(sorted_data) % 2 == 0:
        median_value = (sorted_data[len(sorted_data) // 2 - 1] + sorted_data[len(sorted_data) // 2]) / 2
    else:
        median_value = sorted_data[len(sorted_data) // 2]

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
    for i in range[:len(data) + 1:]:
        pass


    


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    file_obj = open(file)

    for line in file_obj:
        data.append(line.strip())  
    
    # file_obj.close()
    # OR USE TO READ:  BUT WE STILL NEED TO CHANGE THE ITEMS TO A INT AND REMOVE THE \N CHARACTER
    # read_file = file_obj.readlines()
    # data.append(int(read_file.strip()))
    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)

    
    # calculate the average, median, and range of this file using the functions you've wrote
    avg = round(average(cleaned_list), 2)
    med = round(median(cleaned_list), 2)
    rng = round(range(cleaned_list), 2)
    

    # print out your data quality measure to the console

    # print out your descriptive statistics to the console
    print(f"Your heart-rate data average is: {avg}")
    print(f"Your heart-rate data median is: {med}")
    print(f"Your heart-rate data range is: {rng}")
    print('\n')


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
