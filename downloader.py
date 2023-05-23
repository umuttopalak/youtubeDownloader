from pytube import YouTube
import os
import sys
from pytube.exceptions import *

def download(link):
    try:
        yt = YouTube(link)

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        destination = str(os.getcwd()) + "\downloads"

        base, ext = os.path.splitext(video.default_filename)
        mp3_file = base + '.mp3'

        if os.path.exists(mp3_file):
            return "File is already exists"
        
        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        success_message = yt.title + " has been successfully downloaded."
        return success_message

    except VideoUnavailable:
        return "Video is unavailable."

    except RegexMatchError:
        return "Invalid video URL."
    
    except Exception as e:
        return "Beklenmeyen bir hata oluştu: " + str(e)

