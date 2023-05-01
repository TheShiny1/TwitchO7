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

6. Download Python resources.
```
pip install plotly
pip install DateTime
pip install -U scikit-learn
```

7. Run TwitchO7 to collect data. Make sure when you enter in the authorization key that the 'B' in Bearer is capitalized and there is a space between the token_type and and access_token.
```
python TwitchO7.py
```

8. Once you've received a sufficient amount of information from TwitchO7.py, run the analysis program to see all the information that is saved for the day of the week. This is for manual analysis of the user if they don't think Recommendation.py gives correct information
```
python Analysis.py
```
To access file directory, type this:
```
<streamer username>/<day of the week>
```

9. To analyze the data without through an algorithm and receive a recommendation for the times where the streamer's viewer count was above average, run this code:
```
python Recommendation.py
```
To access file directory, type this:
```
<streamer username>/<day of the week>
```

10. To visualize the data

## Results
The results of these tools will give data of the Twitch streamer that they are analyzing to find the time frame when their viewership is above average and a prediction of the average of the next stream. Note that each streamer is different along with each category they stream and that these are recommendations. There is no guarantee that this will increase viewership, only that the tool will give insightful data to the user.
