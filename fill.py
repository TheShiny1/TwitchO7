import os
import pandas as pd
import matplotlib.pyplot as plt

# Set the directory containing the CSV files
directory = 'data/moistcr1tikal/'

# Initialize an empty list to store the timestamps
timestamps = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Read in the CSV file as a pandas dataframe
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)

        # Find the maximum viewer count
        max_viewer_count = df['Viewer Count'].max()

        # Filter the dataframe to show only rows with the maximum viewer count
        max_viewer_rows = df[df['Viewer Count'] == max_viewer_count]

        # Extract the timestamps from the filtered rows and append to the list
        max_viewer_timestamps = max_viewer_rows['Timestamp'].tolist()
        timestamps.extend(max_viewer_timestamps)

# Create a histogram of the timestamps
plt.hist(timestamps, bins=20)
plt.xlabel('Timestamp')
plt.ylabel('Frequency')
plt.show()
