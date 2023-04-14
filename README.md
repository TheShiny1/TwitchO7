# TwitchO7: Using Data to Help Small Streamers Grow on Twitch

## Abstract:
In terms of understanding how growth on Twitch works, there is a substantial knowledge gap in regards to how users are able to grow on the platform. Advice for growth on the platform varies under circumstances from each content creator. For this thesis, I have designed a program that will take information from an online database and the Twitch platform and implement machine learning in order to find an algorithm to maximize channel growth based on timing and category. For the retrieval of online information, I used a tool from the Python programming	language called BeautifulSoup in order to pull the specific information needed such as viewership average and number of average active channels in order to find the ratio between these two factors. From there I ran a program using the tool Pandas in order to create a graph to find spikes in viewership throughout the week. For this section, I’ll be needing to web scrape the HTML code that is accessible through viewing Twitch’s network code and pulling the viewership of the category as it updates throughout the day. That information will then be put into a graph that will update every 5 minutes. Using the ratio of active channels and viewers and running it through the activity of a category, the program will output the optimal times and dates that a user can stream in order to maximize their channel growth as a smaller content creator. 

## Installations
1. Clone Repository.
2. Install cURL using this [link](https://curl.se/download.html).
3. Go to Twitch Developers document [website](https://dev.twitch.tv/docs/authentication/) and follow the instructions to access the Twitch API.
4. When Client ID and Secret are obtained, run this command in your terminal. Replace the words in <> brackets with the tokens from your developer console and remove the brackets
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

5. Once you've received the token type and the access token, save the information 