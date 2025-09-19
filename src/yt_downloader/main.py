import yt_dlp


def fetch_video_list(channel_url):

    ydl_options = {
        "playliststart": 1,
        "playlistend": 1,
        "format": "bestvideo+bestaudio",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "download_archive": "downloaded.txt",

    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download(channel_url)



def download_video(url):

    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)

    ydl_options = {
        "format": "bestvideo+bestaudio",
        "outtmpl": info.get("title")
    }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download(url)

fetch_video_list("https://www.youtube.com/playlist?list=UUuYLDxZWv-aal88czKkFvKA")
# download_video("https://youtu.be/aimvwkuhCIw?si=nmfnAmIcIJnaUNPK")