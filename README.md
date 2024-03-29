# YT_Analysis

Description:
This program retrieves data about channels you're subscribed to (Channel Title, Channe ID, Channel Subscribers, Channel Videos) saves it to a csv file and displays it

Requirements:
- Google Cloud Console project with the YouTube Data API and YouTube Analytics API enabled
- OAuth 2.0 credentials set up for the project
- Python libraries (google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client)

Installation:
1. Download the repository from GitHub.
2. Save OAuth 2.0 credentials in a file named 'credentials.json' in the project directory.
3. Run main.py and give access to your channel data (This will save the data to a csv file named 'subscribed_channels')
4. Run visualize.py (This will display the data)
