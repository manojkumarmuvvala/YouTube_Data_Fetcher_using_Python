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
