from pytube import YouTube
import os
from pytube.exceptions import *

def download(link, lang):
    try:
        yt = YouTube(link)

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        destination = str(os.getcwd()) + f'\{lang["destination"]}'

        base, ext = os.path.splitext(video.default_filename)
        mp3_file = base + '.mp3'

        if os.path.exists(mp3_file):
            return lang["exists"]
        
        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        success_message = yt.title + lang["success_message"]
        return success_message

    except VideoUnavailable:
        return lang["VideoUnavailable"]

    except RegexMatchError:
        return lang["RegexMatchError"]
    
    except Exception as e:
        return lang["Exception"] + str(e)

