import os
import requests
import json
import plotly.graph_objects as go
import datetime
import time
import csv

# Create a directory called "data" if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Set up the Twitch API endpoint and headers
username = input("Enter Streamer's username in the URL: ")
API_ENDPOINT = ("https://api.twitch.tv/helix/streams?user_login=" + username.lowercase())

Client_ID = '9aijwarjiiuslg7ixm1tymagpoo38c'
oauth = 'Bearer xm23gkwmklkbtj1wdbmyxvwt52cdqc'

head = {
  'Client-ID' : Client_ID,
  'authorization' : oauth
}

# Initialize a variable to keep track of the stream status
is_streaming = False

while True:
    # Get the stream data from the Twitch API
    r = requests.get(url = API_ENDPOINT, headers = head)
    json_data = r.text
    data_dict = json.loads(json_data)

    # Check if the stream is currently live
    if data_dict["data"] != [] and not is_streaming:
        print("Stream is now live!")

        # Set the stream status to True and initialize empty lists to store the viewer_count and timestamp
        is_streaming = True
        viewer_count_list = []
        timestamp_list = []
        date_list = []

        # Start fetching viewer count and timestamp data
        while is_streaming:
            r = requests.get(url = API_ENDPOINT, headers = head)
            json_data = r.text
            data_dict = json.loads(json_data)

            if data_dict["data"] == []:
                # Stream is offline, plot the graph, save the data to a CSV file, and set the stream status to False
                fig = go.Figure(data=go.Scatter(x=timestamp_list, y=viewer_count_list, mode='lines'))
                fig.update_layout(title='Viewer Count over Time', xaxis_title='Time of Day', yaxis_title='Viewer Count')
                fig.show()

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H")
                day_of_week = datetime.datetime.today().strftime("%A")
                filename = f"data/{username}/{day_of_week}/{timestamp}.csv"
                if not os.path.exists(f"data/{username}/{day_of_week}"):
                    os.makedirs(f"data/{username}/{day_of_week}")
                with open(filename, mode='w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(['Date', 'Timestamp', 'Viewer Count'])
                    for i in range(len(viewer_count_list)):
                        writer.writerow([date_list[i], timestamp_list[i], viewer_count_list[i]])

                is_streaming = False
            else:
                # Get the viewer_count and current timestamp
                viewer_count = data_dict["data"][0]["viewer_count"]
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                date = datetime.datetime.now().strftime("%Y-%m-%d")

                # Append the viewer_count and timestamp to the respective lists
                viewer_count_list.append(viewer_count)
                timestamp_list.append(timestamp)
                date_list.append(date)


                # Wait for 2 minutes before fetching the viewer count again
                time.sleep(120)
    else:
        # Stream is offline or program is already running, wait for 1 minute before checking again
        time.sleep(60)
