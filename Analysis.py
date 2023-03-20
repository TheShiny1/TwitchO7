import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# read in the csv files and combine them into a single DataFrame
file_names = ['data/moistcr1tikal/viewer_count_data_2023-03-07_22.csv', 'data/moistcr1tikal/viewer_count_data_2023-03-08_22.csv', 'data/moistcr1tikal/viewer_count_data_2023-03-10_11.csv','data/moistcr1tikal/viewer_count_data_2023-03-15 02.csv','data/moistcr1tikal/viewer_count_data_2023-03-19 02.csv']
df = pd.concat([pd.read_csv(file) for file in file_names])

# convert the 'Timestamp' column to datetime and set it as the index
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

# group the data by hour and calculate the mean viewer count
hourly_viewer_count = df.groupby(pd.Grouper(freq='H'))['Viewer Count'].mean()

# create a line plot of the viewer count over time
hourly_viewer_count.plot()
plt.xlabel('Time')
plt.ylabel('Viewer Count')
plt.title('Viewer Count Over Time')
plt.show()

# use linear regression to predict the outcome for the next hour
X = hourly_viewer_count.index.astype(int).values.reshape(-1, 1)
y = hourly_viewer_count.values.reshape(-1, 1)
reg = LinearRegression().fit(X, y)
next_hour = reg.predict([[hourly_viewer_count.index[-1].value + 3600]])
print('Predicted viewer count for the next hour:', next_hour[0][0])
