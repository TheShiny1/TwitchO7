import pandas as pd
import matplotlib.pyplot as plt
import os

# set the path of the directory where the CSV files are located
path = 'data/moistcr1tikal/'

# read all the CSV files in the directory and store them in a list
csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]

# combine all the CSV files into a single dataframe
combined_df = pd.concat([pd.read_csv(os.path.join(path, file)) for file in csv_files])

# calculate the average viewer count of all the CSV files combined
average_viewer_count = combined_df['Viewer Count'].mean()

# create a list to store the average viewer count of each CSV file
average_viewer_counts = []

# loop through the list of CSV files and calculate the average viewer count of each file
for file in csv_files:
    df = pd.read_csv(os.path.join(path, file))
    average_viewer_count_per_file = df['Viewer Count'].mean()
    average_viewer_counts.append(average_viewer_count_per_file)

# plot the average viewer count of each CSV file and the average viewer count of all the CSV files combined
plt.bar(range(len(csv_files)), average_viewer_counts, align='center', alpha=0.5, label='CSV File Average Viewer Count')
plt.axhline(y=average_viewer_count, color='r', linestyle='-', label='Combined Average Viewer Count')
plt.xticks(range(len(csv_files)), csv_files)
plt.xlabel('CSV Files')
plt.ylabel('Average Viewer Count')
plt.title('CSV File Viewer Count Comparison')
plt.legend(loc='best')
plt.show()
