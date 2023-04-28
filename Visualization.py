import os
import pandas as pd
import plotly.graph_objs as go

dir_path = input("Input path to directory that you want to analyze: ")
csv_file_path = input("Enter CSV file path with the CSV file: ")
df = pd.read_csv(csv_file_path)

csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

combined_data = []

for file in csv_files:
    file_path = os.path.join(dir_path, file)
    data = pd.read_csv(file_path)
    combined_data.append(data)

all_data = pd.concat(combined_data)
average_viewer_count = all_data["Viewer Count"].mean()

timestamp_list = pd.to_datetime(df['Timestamp'])
viewer_count_list = df['Viewer Count']

fig = go.Figure(data=go.Scatter(x=timestamp_list, y=viewer_count_list, mode='lines'))
fig.add_hline(y=average_viewer_count, line_dash="dot", line_color="red",
              annotation_text=f"Average Viewer Count: {average_viewer_count:.2f}")
fig.update_layout(title='Viewer Count over Time', xaxis_title='Time of Day', yaxis_title='Viewer Count')

fig.show()
