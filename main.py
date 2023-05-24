import tkinter as tk
from link_checker import link_checker
from downloader import download
import languages.en as en
import languages.tr as tr
import language_utils as lang_utils

window = tk.Tk()
window.title("MP3 Downloader")
window.geometry("800x200")
window.resizable(False, False)


def on_click_btn1():
    if link_checker(str(input.get())):
        result = download(str(input.get()) , lang_utils.get_translation(languagesMenu.get()))
        label.config(text=result)


label = tk.Label(window, text="Enter the music link then click the download button", font=('Calibri 15 bold'))
label.pack(pady=20)


frame = tk.Frame(window)
frame.pack()

input = tk.Entry(frame, width=50)
input.pack(side="left", padx=10)


btn1 = tk.Button(frame, text="Download", command=on_click_btn1)
btn1.pack(side="left", padx=10)

languagesMenu = tk.StringVar()
languagesMenu.set("Select any language")

drop = tk.OptionMenu(window , languagesMenu , "TR" , "EN")
drop.pack(side="right" , padx=20)


languagesMenu.trace("w", lambda *args: lang_utils.on_language_change(languagesMenu, label, btn1))

window.mainloop()