import tkinter as tk
from link_checker import link_checker
from downloader import download

window = tk.Tk()
window.title("MP3 Downloader")
window.geometry("800x200")
window.resizable(False, False)


def on_click_btn1():
    if link_checker(str(input.get())):
        result = download(str(input.get()))
        label.config(text=result)


label = tk.Label(window, text="Enter the music link then click the download button", font=('Calibri 15 bold'))
label.pack(pady=20)


frame = tk.Frame(window)
frame.pack()

input = tk.Entry(frame, width=50)
input.pack(side="left", padx=10)


btn1 = tk.Button(frame, text="Download", command=on_click_btn1)
btn1.pack(side="left", padx=10)

window.mainloop()