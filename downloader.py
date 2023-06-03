from pytube import YouTube
import os
from pytube.exceptions import * 
from showThumbnail import show

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
        return lang["exists"]
    except VideoUnavailable:
        return lang["VideoUnavailable"]

    except RegexMatchError:
        return lang["RegexMatchError"]
    
    except Exception as e:
        print(str(e))
        return lang["Exception"] + str(e)

