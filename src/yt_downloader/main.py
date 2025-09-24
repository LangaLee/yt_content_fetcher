import yt_dlp
import questionary


with open("../../subs.txt","r") as f:
    usual_suspects = f.read().split("\n")


def download_multiple_videos(channels,end):
    urls = [f"{chan}/videos" for chan in channels]
    ydl_options = {
        "playliststart": 1,
        "playlistend": end,
        "format": "bestvideo+bestaudio",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "download_archive": "downloaded.txt",

    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download(urls)



def download_video(url):

    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)

    ydl_options = {
        "format": "bestvideo+bestaudio",
        "outtmpl": f"downloads/{info.get("title")}"
    }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download(url)


def update_library():
    choice = questionary.select(
        "Donwload multiple or single",
        choices=["single", "multiple","update"]
    ).ask()
    
    yt_link = input("please enter video or channel link here: \n")


    # making sure that we just get the pure channel link so we can save it later
    if yt_link.endswith("/videos"):
        yt_link = f"{yt_link[:yt_link.rfind("/videos")]}\n"

    if choice == "single":
        download_video(yt_link)
    elif choice == "multiple":
        end = input("num of videos: \n")
        download_multiple_videos([yt_link],int(end))
        if yt_link in usual_suspects:
            print("channel already recorded")
            return
        with open("../../subs.txt","a") as f:
            f.write(yt_link)
        
            
    elif choice == "update":
        download_multiple_videos(usual_suspects,5)

#https://www.youtube.com/playlist?list=UUuYLDxZWv-aal88czKkFvKA
update_library()