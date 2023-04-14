# TwitchO7: Using Data to Help Small Streamers Grow on Twitch

## Abstract:
In terms of understanding how growth on Twitch works, there is a substantial knowledge gap in regards to how users are able to grow on the platform. Advice for growth on the platform varies under circumstances from each content creator. For this thesis, I have designed a program that will take information from an online database and the Twitch platform and implement machine learning in order to find an algorithm to maximize channel growth based on timing and category. For the retrieval of online information, I used a tool from the Python programming	language called BeautifulSoup in order to pull the specific information needed such as viewership average and number of average active channels in order to find the ratio between these two factors. From there I ran a program using the tool Pandas in order to create a graph to find spikes in viewership throughout the week. For this section, I’ll be needing to web scrape the HTML code that is accessible through viewing Twitch’s network code and pulling the viewership of the category as it updates throughout the day. That information will then be put into a graph that will update every 5 minutes. Using the ratio of active channels and viewers and running it through the activity of a category, the program will output the optimal times and dates that a user can stream in order to maximize their channel growth as a smaller content creator. 

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

## Results
The results of these tools will give data of the Twitch streamer that they are analyzing to find the time frame when their viewership is above average. Note that each streamer is different along with each category they stream and that these are recommendations. There is no guarantee that this will increase viewership, only that the tool will give insightful data to the user.