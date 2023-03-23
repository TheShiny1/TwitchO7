import os
import pandas as pd

dir_path = input("Input path to directory that you want to analyze: ")

csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

combined_data = []

for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    combined_data.append(data)


all_data = pd.concat(combined_data)

average_viewer_count = all_data["Viewer Count"].mean()

print("The average viewer count of all the csv files combined is:", average_viewer_count)

above_average_data = all_data[all_data["Viewer Count"] > average_viewer_count]

if not above_average_data.empty:
    print("Timestamps where viewer count is higher than the average:")
    
    above_average_data.reset_index(drop=True, inplace=True)
    end_timestamp = above_average_data.iloc[0]["Timestamp"]
    start_timestamp = above_average_data.iloc[-1]["Timestamp"]
    print("Start timestamp:", start_timestamp)
    print("End timestamp:", end_timestamp)
    

else:
    print("There is no data where viewer count is higher than the average.")
