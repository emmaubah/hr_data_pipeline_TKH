from statistical import average, median, range, variance, standard_dev, line_chart
from data_cleaning import clean_heartrate_data 


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
    var = round(variance(cleaned_list), 2)
    std = round(standard_dev(cleaned_list), 2)
    
    
    # print out your data quality measure to the console

    # print out your descriptive statistics to the console
    print(f"Your heart-rate data average is: {avg}")
    print(f"Your heart-rate data median is: {med}")
    print(f"Your heart-rate data range is: {rng}")
    print(f"Your heart-rate data variance is: {var}")
    print(f"Your heart-rate data standard deviation is: {std}")
    print(line_chart(cleaned_list))
    print()
    


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
