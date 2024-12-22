# YouTube_Data_Fetcher_using_Python
# Project Description
The YouTube Data Fetcher is a Python-based application that utilizes the YouTube Data API v3 to fetch detailed information about videos of a specific genre. This application retrieves metadata such as video title, description, tags, view count, comment count, duration, and more. The data is processed and saved into a CSV file for further analysis.

# Features
Fetches up to 500 top-viewed videos for a given genre.
Extracts detailed video metadata, including:
Video URL
Title and Description
Channel Name
Keyword Tags
Category ID
View and Comment Counts
Duration
Location and Captions (if available)
Topic Categories
Handles missing data gracefully by replacing it with default values.
Saves the fetched data into a CSV file for easy access and analysis.

# How It Works
The user provides a genre as input.
The script interacts with the YouTube Data API v3 to:
Fetch video IDs using a search query for the given genre.
Fetch detailed metadata for each video in batches.
For videos with captions, it fetches the transcription using the YouTube Transcript API.
Processes the data and saves it to a CSV file.

# Requirements
Python 3.8 or later
Libraries:
google-api-python-client (for YouTube Data API interactions)
youtube-transcript-api (for fetching video captions)
pandas (for data processing)

# Setup and Installation
Clone the repository or download the project files.
Install the required libraries:
pip install google-api-python-client youtube-transcript-api pandas
Replace the API_KEY variable with your own YouTube API Key:
API_KEY = "YOUR_YOUTUBE_API_KEY"

# Usage
Run the main() function:
python your_script_name.py
Enter the genre for which you want to fetch video data.
The script will process the videos and save the results in a CSV file named <genre>_videos.csv.

# Error Handling
Missing API Key: Ensure the API_KEY variable contains a valid YouTube API Key.
Invalid Input: The script requires a valid genre as input.
API Quota Limit: If the API quota is exceeded, you will need to wait or use a different API key.

# Output Example
The final CSV file will include the following columns:
Video URL
Title
Description
Channel Title
Keyword Tags
YouTube Video Category
Topic Details
Video Published At
Video Duration
View Count
Comment Count
Captions Available
Location of Recording
Caption Text

# Future Enhancements
Add support for fetching more than 500 videos by handling pagination.
Include additional filtering options for better control over the search results.
Implement visualization tools for analyzing the fetched data.
