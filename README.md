
# Pinterest Video Downloader

A simple Python script that uses `yt-dlp` to download videos from Pinterest by providing a video URL.

## Features
- Allows downloading Pinterest videos using a URL.
- Provides an option to download multiple videos by entering multiple URLs in succession.
- Simple CLI interface.

## Prerequisites
- **Python 3.7+** required.
- **yt-dlp**: Install it via pip.

  ```bash
  pip install yt-dlp
  ```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/its-cutie-valerie/pinterest-video-downloader.git
   cd pinterest-video-downloader
   ```

2. Run the script:

   ```bash
   python pinterest_downloader.py
   ```

3. When prompted, enter the Pinterest video URL you want to download. Type `no` to exit.

   ```
   Enter the Pinterest video URL you want to download (or type 'no' to exit): [Your Pinterest URL here]
   ```

4. Your video will download to the current directory with the video ID as the filename.

## Example

```plaintext
Enter the Pinterest video URL you want to download (or type 'no' to exit): https://www.pinterest.com/pin/123456789/
```

## Notes
This script is intended for personal use only. Always respect copyright laws and Pinterest's terms of service when downloading videos.

