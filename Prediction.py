import os
import pandas as pd

dir_path = input("Input path to directory that you want to analyze: ")

csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

combined_data = []

# loop through the csv files and append their data to the combined_data list
for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    combined_data.append(data)

all_data = pd.concat(combined_data)

average_viewer_count = all_data["Viewer Count"].mean()

timestamp_list = []

# loop through the csv files again and find the timestamps where the viewer count is higher than the average
for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    above_average_data = data[data["Viewer Count"] > average_viewer_count]
    if not above_average_data.empty:
        above_average_data.reset_index(drop=True, inplace=True)
        start_timestamp = above_average_data.iloc[0]["Timestamp"]
        end_timestamp = above_average_data.iloc[-1]["Timestamp"]
        timestamp_list.append([start_timestamp, end_timestamp])

# calculate the mean of the start and end timestamps where the viewer count is higher than the average
if timestamp_list:
    timestamp_list = pd.DataFrame(timestamp_list, columns=["Start Timestamp", "End Timestamp"])
    mean_start_timestamp = timestamp_list["Start Timestamp"].apply(pd.to_timedelta).mean()
    mean_end_timestamp = timestamp_list["End Timestamp"].apply(pd.to_timedelta).mean()

    print("Mean start timestamp:", str(mean_start_timestamp))
    print("Mean end timestamp:", str(mean_end_timestamp))
else:
    print("No timestamps found where viewer count is higher than the average.")
