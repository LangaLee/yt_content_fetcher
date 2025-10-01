import yt_dlp

CHANNEL_FOLDERS = {
    "https://www.youtube.com/@AfterDark": "/media/youtube/AfterDark/Season 01",
    "https://www.youtube.com/@KaiLentit": "/media/youtube/Kai Lentit/Season 01",
    "https://www.youtube.com/@Livakivi": "/media/youtube/Livakivi/Season 01",
    "https://www.youtube.com/@NERDULT": "/media/youtube/NERDULT/Season 01",
    "https://www.youtube.com/@Nghtshtrs": "/media/youtube/Nghtshtrs/Season 01",
    "https://www.youtube.com/@Nightride": "/media/youtube/Nightride/Season 01",
    "https://www.youtube.com/@NPRMusic": "/media/youtube/NPR Music/Season 01",
    "https://www.youtube.com/@The_FirstTake": "/media/youtube/The First Take/Season 01",
}

def download_multiple_videos():
    for chan, folder in CHANNEL_FOLDERS.items():

        ydl_options = {
            "writesubtitles":True,
            "subtitleslangs": ["en","ja"],
            "subtitlesformat": "best",
            "writeautomaticsub": True,
            "embedsubtitles": True,
            "playliststart": 1,
            "playlistend": 5,
            "format": "bestvideo+bestaudio",
            "outtmpl": f"{folder}/%(upload_date>%Y-%m-%d)s - %(title).200B.%(ext)s",
            "download_archive": "downloaded.txt",
            "ignoreerrors":True
        }
        print(ydl_options["outtmpl"])
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download(chan)


download_multiple_videos()