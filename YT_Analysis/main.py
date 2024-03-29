import os
import csv
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import googleapiclient.errors

# Define the scopes required for the YouTube Data API and YouTube Analytics API
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def authenticate():
    """Authenticate using OAuth2"""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = google.oauth2.credentials.Credentials.from_authorized_user_file('token.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Print the URI being used for the authorization request
            print("Authorization URI:", 'http://localhost:50715')
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES,
                redirect_uri='http://localhost:50715')
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_subscribed_channels():
    """Get data about the channels the user is subscribed to"""
    # Authenticate using OAuth2
    credentials = authenticate()
    # Build the YouTube Data API service
    youtube = build('youtube', 'v3', credentials=credentials)
    
    try:
        # Initialize variables for pagination
        next_page_token = None
        all_subscriptions = []

        # Continue paginating until all subscriptions are retrieved
        while True:
            # Get the user's subscriptions
            subscriptions_response = youtube.subscriptions().list(
                mine=True,
                part='snippet',
                maxResults=50,  # Adjust as needed, 50 is the maximum allowed
                pageToken=next_page_token
            ).execute()

            # Append the subscriptions to the list
            if 'items' in subscriptions_response:
                all_subscriptions.extend(subscriptions_response['items'])

            # Check if there are more subscriptions to retrieve
            next_page_token = subscriptions_response.get('nextPageToken')
            if not next_page_token:
                break

        # Prepare CSV file
        csv_file = 'subscribed_channels.csv'
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Channel Title', 'Channel ID', 'Channel Views', 'Channel Subscribers', 'Channel Videos'])
            
            # Retrieve details for each subscribed channel
            for item in all_subscriptions:
                snippet = item.get('snippet', {})
                channel_title = snippet.get('title', 'Unknown')
                channel_id = snippet.get('resourceId', {}).get('channelId', 'Unknown')

                # Fetch details of the subscribed channel
                channel_response = youtube.channels().list(
                    id=channel_id,
                    part='snippet,statistics'
                ).execute()

                if 'items' in channel_response:
                    channel_data = channel_response['items'][0]
                    statistics = channel_data.get('statistics', {})

                    # Write data to CSV
                    writer.writerow([
                        channel_title,
                        channel_id,
                        statistics.get('viewCount', 'Unknown'),
                        statistics.get('subscriberCount', 'Unknown'),
                        statistics.get('videoCount', 'Unknown')
                    ])
                
        print("Subscribed channels data saved to:", csv_file)

    except googleapiclient.errors.HttpError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_subscribed_channels()
