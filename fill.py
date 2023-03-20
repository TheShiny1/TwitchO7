import pandas as pd
import matplotlib.pyplot as plt
import glob

# Step 1
# Import necessary libraries

# Step 2
# Read all csv files from a directory
all_files = glob.glob("data/moistcr1tikal/*.csv")
df_list = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df_list.append(df)

# Step 3
# Concatenate all csv files into a single dataframe
df = pd.concat(df_list, axis=0, ignore_index=True)

# Step 4
# Convert the 'Timestamp' column to datetime object and set it as the index of the dataframe
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.set_index('Timestamp')

# Step 5
# Resample the data by hour and get the mean value for each hour
df_hourly = df.resample('H').mean()

# Step 6
# Plot the graph with the viewer count on the y-axis and the datetime on the x-axis
plt.plot(df_hourly.index, df_hourly['Viewer Count'])
plt.xlabel('Date')
plt.ylabel('Viewer Count')
plt.title('Viewer Count per Hour')
plt.show()

# Step 7
# Get the last timestamp from the dataframe and add one hour to it
last_timestamp = df_hourly.index[-1]
next_timestamp = last_timestamp + pd.Timedelta(hours=1)

# Step 8
# Predict the outcome of the viewer count for the next csv file for the next hour
next_viewer_count = df_hourly.loc[last_timestamp]['Viewer Count']
print("The predicted viewer count for the next hour is:", next_viewer_count)
