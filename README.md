# TwitchO7: Using Data to Help Streamers Grow on Twitch

## Installations
1. Clone Repository.
2. Install cURL using this [link](https://curl.se/download.html).
3. Go to Twitch Developers document [website](https://dev.twitch.tv/docs/authentication/) and follow the instructions to access the Twitch API.
4. When Client ID and Secret are obtained, run this command in your terminal. Replace the words in <> brackets with the tokens from your developer console and remove the brackets.
Windows: 
```
curl -X POST "https://id.twitch.tv/oauth2/token" -H "Content-Type: application/x-www-form-urlencoded" -d "client_id=<your client id goes here>&client_secret=<your client secret goes here>&grant_type=client_credentials"
```

MacOS:
```
curl -X POST 'https://id.twitch.tv/oauth2/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'client_id=<your client id goes here>&client_secret=<your client secret goes here>&grant_type=client_credentials'
```

5. Once you've received the token type and the access token, save the keys and tokens to a document that you can access for future reference.

## Running the program
1. Download Python resources.
```
pip install plotly
pip install DateTime
pip install -U scikit-learn
```

2. Run TwitchO7 to collect data. Make sure when you enter in the authorization key that the 'B' in Bearer is capitalized and there is a space between the token_type and and access_token.
```
python TwitchO7.py
```

3. Once you've received a sufficient amount of information from TwitchO7.py, run the analysis program to see all the information that is saved for the day of the week. This is for manual analysis of the user if they don't think Recommendation.py gives correct information
```
python Analysis.py
```
To access file directory, type this:
```
data/<streamer username>/<day of the week>
```

4. To analyze the data without through an algorithm and receive a recommendation for the times where the streamer's viewer count was above average, run this command:
```
python Recommendation.py
```
To access file directory, type this:
```
data/<streamer username>/<day of the week>
```

5. To visualize the data by seeing the trend in data and comparing it to the average viewer count of that day of the week, type this command:
```
python Visualization.py
```
To access file directory, type this:
```
data/<streamer username>/<day of the week>
```

6. Lastly, to see the general trend in data regarding viewership averge for this day, run this command:
```
python predictAvg.py
```
To access file directory, type this:
```
data/<streamer username>/<day of the week>
```


## Results
The results of these tools will give data of the Twitch streamer that they are analyzing to find the time frame when their viewership is above average and a prediction of the average of the next stream. Note that each streamer is different along with each category they stream and that these are recommendations. There is no guarantee that this will increase viewership, only that the tool will give insightful data to the user.
