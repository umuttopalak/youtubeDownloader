from PIL import Image , ImageTk
from urllib.request import urlopen

def show(url , photoLabel):
    u = urlopen(url)
    raw_data = u.read()
    u.close()
    
    photo = ImageTk.PhotoImage(data=raw_data)
    photoLabel.image = photo

    