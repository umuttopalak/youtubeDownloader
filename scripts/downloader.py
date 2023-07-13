import os

from pytube import YouTube
from pytube.exceptions import *

from scripts.showThumbnail import show


def download(link, lang):
    try:
        yt = YouTube(link)
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        destination = str(os.getcwd()) + f'\{lang["destination"]}'

        base, ext = os.path.splitext(video.default_filename)
        mp3_file = base + '.mp3'


        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        success_message = yt.title + lang["success_message"]
        return success_message

    except FileExistsError:
        print("dosya zaten var")
        return lang["exists"]
    except VideoUnavailable:
        print("video yok diyo la")
        return lang["VideoUnavailable"]

    except RegexMatchError:
        print("regex ney")
        return lang["RegexMatchError"]
    
    except Exception as e:
        print(str(e) , "\n Bilinmeyen hata")
        
        return lang["Exception"] + str(e)

