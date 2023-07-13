import tkinter as tk

import languages.en as en
import languages.tr as tr
import scripts.language_utils as lang_utils
from scripts.downloader import download
from scripts.link_checker import link_checker
from scripts.showThumbnail import show

window = tk.Tk()
window.title("MP3 Downloader")
window.geometry("800x200")
window.resizable(False, False)


def on_click_btn1():
    if link_checker(str(input.get())):
        result = download(str(input.get()) , lang_utils.get_translation(languagesMenu.get()))
        label.config(text=result)
        

languagesMenu = tk.StringVar()

photoLabel = tk.Label()
photoLabel.pack(side="top")

label = tk.Label(window, text=lang_utils.get_translation(languagesMenu.get())['label_text'], font=('Calibri 15 bold'))
label.pack(pady=20)


frame = tk.Frame(window)
frame.pack()

input = tk.Entry(frame, width=50)
input.pack(side="left", padx=10)


btn1 = tk.Button(frame, text=lang_utils.get_translation(languagesMenu.get())['button_text'], command=on_click_btn1)
btn1.pack(side="left", padx=10)


languagesMenu.set("Select Language")

drop = tk.OptionMenu(window , languagesMenu , "TR" , "EN")
drop.pack(side="right" , padx=20)



languagesMenu.trace("w", lambda *args: lang_utils.on_language_change(languagesMenu, label, btn1))

window.mainloop()