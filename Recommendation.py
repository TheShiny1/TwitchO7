import os
import pandas as pd
from statistics import mode

# set the directory path
dir_path = input("Input path to directory that you want to analyze: ")

# read all csv files in the directory
csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

# create an empty list to store the combined data from all files
combined_data = []

# loop through the csv files and append their data to the combined_data list
for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    combined_data.append(data)

# combine all the data from the csv files
all_data = pd.concat(combined_data)

# calculate the average viewer count of all the csv files combined
average_viewer_count = all_data["Viewer Count"].mean()

# print out the average viewer count
print("The average viewer count of all the csv files combined is:", average_viewer_count)

timestamps = pd.DataFrame(columns=['Start Timestamp', 'End Timestamp'])

# loop through the csv files again and find the timestamps where the viewer count is higher than the average
for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    above_average_data = data[data["Viewer Count"] > average_viewer_count]
    if not above_average_data.empty:
        # find the start and end timestamp where the viewer count is higher than the average
        above_average_data.reset_index(drop=True, inplace=True)
        start_timestamp = above_average_data.iloc[0]["Timestamp"]
        end_timestamp = above_average_data.iloc[-1]["Timestamp"]
        timestamps = timestamps.append({'Start Timestamp': start_timestamp, 'End Timestamp': end_timestamp}, ignore_index=True)

# calculate the median of the start and end timestamps
median_start_timestamp = pd.to_datetime(timestamps['Start Timestamp']).median().strftime('%H:%M:%S')
median_end_timestamp = pd.to_datetime(timestamps['End Timestamp']).median().strftime('%H:%M:%S')

# print out the median start and end timestamps
print("Median start timestamp where viewer count is higher than the average:", median_start_timestamp)
print("Median end timestamp where viewer count is higher than the average:", median_end_timestamp)