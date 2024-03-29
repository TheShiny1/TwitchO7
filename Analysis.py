import os
import pandas as pd

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

for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    file_average_viewer_count = data["Viewer Count"].mean()
    print(f"The average viewer count of {file} is:", file_average_viewer_count)

# loop through the csv files again and find the timestamps where the viewer count is higher than the average
for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    above_average_data = data[data["Viewer Count"] > average_viewer_count]
    if not above_average_data.empty:
        print("Timestamps in file", file, "where viewer count is higher than the average:")
        
        # find the start and end timestamp where the viewer count is higher than the average
        above_average_data.reset_index(drop=True, inplace=True)
        start_timestamp = above_average_data.iloc[0]["Timestamp"]
        end_timestamp = above_average_data.iloc[-1]["Timestamp"]
        print("Start timestamp:", start_timestamp)
        print("End timestamp:", end_timestamp)
