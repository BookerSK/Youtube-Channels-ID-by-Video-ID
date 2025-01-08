import requests, time
from bs4 import BeautifulSoup
import re
import csv

def get_channel_id(video_url):
    # Send an HTTP GET request to the YouTube video URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    response = requests.get(video_url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve the page for {video_url}")
        return None

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Try to find the channelId in the page source
    match = re.search(r'channelId":"([^"]+)"', str(soup))

    if match:
        channel_id = match.group(1)
        return channel_id
    else:
        print(f"Channel ID not found for {video_url}")
        return None


def process_csv(input_file, output_file):
    # Open the input CSV file and read the video IDs
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write the header for the output file
        writer.writerow(["Video ID", "Channel ID"])

        for row in reader:
            video_id = row[0]  # assuming video ID is in the first column
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"Processing {video_url}...")
            channel_id = get_channel_id(video_url)
            if channel_id:
                writer.writerow([video_id, channel_id])
            else:
                writer.writerow([video_id, "Not Found"])
            time.sleep(1)

# Example usage:
input_file = 'input.csv'  # Your input CSV file containing YouTube video IDs
output_file = 'output.csv'  # Output CSV file with channel IDs

process_csv(input_file, output_file)
print("Processing complete!")
