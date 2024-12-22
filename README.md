# YouTube Data Fetcher
## Project Description
The **YouTube Data Fetcher** is a Python-based application that uses the **YouTube Data API v3** to fetch detailed information about videos from a specific genre. The application extracts metadata like video titles, descriptions, view counts, comment counts, durations, and more. This data is then saved to a CSV file for analysis.
## Features
- Fetches up to 500 top-viewed videos from a given genre.
- Retrieves detailed video information, including:
  - Video URL
  - Title and Description
  - Channel Name
  - Keyword Tags
  - Category ID
  - View and Comment Counts
  - Duration
  - Location and Captions (if available)
  - Topic Categories
- Handles missing data by filling with default values.
- Saves fetched data into a **CSV file** for easy access.
## How It Works
1. The user provides a **genre** as input.
2. The script uses the **YouTube Data API v3** to fetch:
   - Video IDs related to the given genre.
   - Detailed metadata for each video in batches.
3. The script checks if captions are available for each video and retrieves the transcriptions using the **YouTube Transcript API**.
4. Processes the video data and saves it to a CSV file.
## Requirements
- Python 3.8 or later
- Python libraries:
  - `google-api-python-client`
  - `youtube-transcript-api`
  - `pandas`
## Setup and Installation
### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```
## Usage
Run the script:
- python youtube_scraper.py
- The script will prompt you to enter a genre (e.g., "technology", "music", etc.). It will then fetch the top 500 videos for that genre based on view count.
- The script will collect various details for each video and save them in a CSV file. The file will be saved with the format genre_videos.csv in the same directory.

# Example Output: 
- After the script completes, you will have a CSV file containing the following columns:
  - Video URL: Direct URL to the video.
  - Title: Title of the video.
  - Description: Description of the video.
  - Channel Title: Name of the channel.
  - Keyword Tags: Tags associated with the video.
  - YouTube Video Category: Category ID of the video.
  - Topic Details: Relevant topics/categories for the video.
  - Video Published At: Date and time the video was published.
  - Video Duration: Duration of the video.
  - View Count: Number of views.
  - Comment Count: Number of comments.
  - Captions Available: Whether captions are available for the video.
  - Location of Recording: Location where the video was recorded.
  - Caption Text: Transcript text, if captions are available.
## Future Work
- **Expand Data Fields**: Currently, the script fetches basic video details. Future work can include fetching additional information such as the video's likes/dislikes, playlist information, and related videos.

- **Error Handling**: Although basic error handling exists (e.g., in the check_captions() function), more robust error handling for API calls, network issues, and edge cases can be added.

- **Optimize Data Fetching**: The script currently fetches video data in batches of 50. There could be optimization for handling rate limits and fetching data in parallel to speed up the process.

- **User Interface**: A simple web or desktop interface can be developed for ease of use, allowing users to select a genre and view the results directly in the interface.

- **Analytics and Visualizations**: Additional features could be added to perform data analysis and generate visualizations based on the video data, such as trending topics or video performance over time.


