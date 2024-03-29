import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('subscribed_channels.csv')

# Sort the DataFrame by 'Channel Subscribers' column in descending order
df_sorted = df.sort_values(by='Channel Subscribers', ascending=False)

# Display the sorted DataFrame
print(df_sorted)

# Print the channel with the most subscribers
most_subscribers_channel = df_sorted.iloc[0]  # First row has the highest subscriber count
print("Channel with the most subscribers:")
print("Name:", most_subscribers_channel['Channel Title'])
print("Subscribers:", most_subscribers_channel['Channel Subscribers'])
print()

# Print the channel with the least subscribers
least_subscribers_channel = df_sorted.iloc[-1]  # Last row has the lowest subscriber count
print("Channel with the least subscribers:")
print("Name:", least_subscribers_channel['Channel Title'])
print("Subscribers:", least_subscribers_channel['Channel Subscribers'])
print()

# Find and print the channel with the most views
max_views_channel = df.loc[df['Channel Views'].idxmax()]
print("Channel with the most views:")
print("Name:", max_views_channel['Channel Title'])
print("Views:", max_views_channel['Channel Views'])
print()

# Find and print the channel with the least views
min_views_channel = df.loc[df['Channel Views'].idxmin()]
print("Channel with the least views:")
print("Name:", min_views_channel['Channel Title'])
print("Views:", min_views_channel['Channel Views'])
print()

# Find and print the channel with the most videos
max_videos_channel = df.loc[df['Channel Videos'].idxmax()]
print("Channel with the most videos:")
print("Name:", max_videos_channel['Channel Title'])
print("Videos:", max_videos_channel['Channel Videos'])
print()

# Find and print the channel with the least videos
min_videos_channel = df.loc[df['Channel Videos'].idxmin()]
print("Channel with the least videos:")
print("Name:", min_videos_channel['Channel Title'])
print("Videos:", min_videos_channel['Channel Videos'])
print()

# Calculate and print the median number for each metric
median_subscribers = df['Channel Subscribers'].median()
median_views = df['Channel Views'].median()
median_videos = df['Channel Videos'].median()
print("Median number of subscribers:", median_subscribers)
print("Median number of views:", median_views)
print("Median number of videos:", median_videos)

# Example visualizations
# Create a bar plot to visualize the number of subscribers for each channel
df_sorted.plot(x='Channel Title', y='Channel Subscribers', kind='bar', legend=False, title='Number of Subscribers for each Channel')
