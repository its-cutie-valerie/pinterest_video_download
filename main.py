import yt_dlp

def download_pinterest_video(url):
    ydl_opts = {
        'outtmpl': '%(id)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    while True:
        pinterest_url = input("Enter the Pinterest video URL you want download (or type 'no' to exit): ")
        if pinterest_url.lower() == 'no':
            print("Goodbye!")
            break
        download_pinterest_video(pinterest_url)

main()
