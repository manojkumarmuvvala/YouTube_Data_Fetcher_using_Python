import pandas as pd
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your YouTube API Key
API_KEY = "Your_Youtube_API_key"

# Fetch video IDs from a genre, sorted by view count (Top videos)
def fetch_video_ids(genre, max_results=500):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    video_ids = []
    next_page_token = None

    while len(video_ids) < max_results:
        request = youtube.search().list(
            part="id,snippet",
            q=genre,
            type="video",
            maxResults=min(50, max_results - len(video_ids)),
            pageToken=next_page_token,
            order="viewCount"  # Ensure sorting by view count
        )
        response = request.execute()

        for item in response["items"]:
            video_ids.append(item["id"]["videoId"])

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return video_ids

# Fetch detailed information about each video
def fetch_video_details(video_ids):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    video_data = []
    processed_cnt = 0

    # Request video details in batches of 50
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics,recordingDetails,topicDetails",
            id=",".join(video_ids[i:i + 50])
        )
        response = request.execute()

        for idx, item in enumerate(response["items"], start=1):
            processed_cnt += 1
            print(f"Processing video {processed_cnt} / {len(video_ids)}")

            snippet = item["snippet"]
            content_details = item["contentDetails"]
            statistics = item["statistics"]
            recording_details = item.get("recordingDetails", {})
            topic_details = item.get("topicDetails", {})

            # Ensure that we handle missing data gracefully
            video_data.append({
                "Video URL": f"https://www.youtube.com/watch?v={item['id']}",
                "Title": snippet["title"],
                "Description": snippet.get("description", "N/A"),
                "Channel Title": snippet["channelTitle"],
                "Keyword Tags": ", ".join(snippet.get("tags", [])) if snippet.get("tags") else "N/A",
                "YouTube Video Category": snippet.get("categoryId", "N/A"),
                "Topic Details": ", ".join(topic_details.get("topicCategories", [])) if topic_details.get("topicCategories") else "N/A",
                "Video Published At": snippet["publishedAt"],
                "Video Duration": content_details.get("duration", "N/A"),
                "View Count": statistics.get("viewCount", "0"),
                "Comment Count": statistics.get("commentCount", "0"),
                "Captions Available": check_captions(item['id']),
                "Location of Recording": recording_details.get("locationDescription", "N/A"),
                "Caption Text": get_caption_text(item['id']) if check_captions(item['id']) else "N/A",
            })
    return video_data

# Check if captions are available
def check_captions(video_id):
    try:
        YouTubeTranscriptApi.get_transcript(video_id)
        return True
    except:
        return False

# Fetch captions text
def get_caption_text(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item["text"] for item in transcript])
    except:
        return "N/A"

# Save the data to a CSV file
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
        # Handle missing values
    df['Description'].fillna("No description provided", inplace=True)
    df['Keyword Tags'].fillna("No tags provided", inplace=True)
    df['Topic Details'].fillna("No topics provided", inplace=True)
    df['Location of Recording'].fillna("No location detected", inplace=True)
    df['Caption Text'].fillna("No captions available", inplace=True)
    df.to_csv(filename, index=False)
    print(f"Saved data to {filename}")

# Main function to run the process
def main():
    genre = input("Enter a genre: ")
    print("Fetching video IDs...")
    video_ids = fetch_video_ids(genre)
    
    print("Fetching video details...")
    video_details = fetch_video_details(video_ids)
    
    print("Saving data to CSV...")
    save_to_csv(video_details, f"{genre}_videos.csv")

if __name__ == "__main__":
    main()
