# YouTube Channel ID Scraper

This Python script extracts YouTube Channel IDs for a list of video IDs and writes the results to a CSV file. The script retrieves channel IDs by scraping the page source of YouTube videos, then extracts the `channelId` from the HTML content using regular expressions.

## Features:
- Extract YouTube Channel IDs from video pages.
- Supports bulk processing of video IDs from a CSV file.
- Writes results to a CSV file containing both Video ID and Channel ID.
- Includes basic error handling and rate-limiting to avoid server overload.

## Prerequisites
To run this script, you will need to have Python installed along with a couple of required libraries.

### Required Libraries:
- `requests`
- `beautifulsoup4`
- `re`
- `csv`
- `time`

You can install the required libraries using the following:

```bash
pip install requests beautifulsoup4
