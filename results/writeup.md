1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

FILE 2: Range: 54, Median: 88.5, Average: 87.3
FILE 3: {Average: 85.18, Median: 85, Range: 63}
The results from these two datasets seem to demonstrate the most active time in a 30-year-old's heart rate; file 2's average and median are roughly equal, suggesting that the data exhibits symmetric behavior. The values output are closest to the workout zone for that age range, but the spread for file 3 range results may lead to unreliable data results.

2) Which file had the **poorest** data quality? How do you know?
The range for file 3, which is 63, indicates a potential spread of the dataset; nevertheless, this finding of such a large range has little bearing on the datasets as a whole and may indicate an outliner or inconsistent data measurement. Because of the excessive spread, the data may be less useful.

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
Range = max - min --> 180 - 68 = 112


b) Explain how the extreme value affects the range.
An extreme value, such as 180, causes an outlier in the dataset. As a result, the extreme value has an impact on the range since it increases the range and fails to provide the true distribution of the dataset.


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
The Interquartile Range (IQR), which focuses on 50% of the data and provides a more accurate spread, is an alternative statistic that represents the usual variability and avoids extreme values (outliers) to measure the spread of the dataset.
