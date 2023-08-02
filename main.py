import tkinter
import customtkinter
from pytube import YouTube
from tkinter import messagebox


def startDownload():
    try:
        ytlink = link.get()
        ytObject =YouTube(ytlink,on_progress_callback = on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="Downloading...", text_color="blue")
        download_button.configure(state=tkinter.DISABLED)
        video.download()
        finishlabel.configure(text="Downloaded", text_color="green")
        download_button.configure(state=tkinter.NORMAL)
    except Exception as e:
        finishlabel.configure(text="Download Error", text_color="red")
        download_button.configure(state=tkinter.NORMAL)
        messagebox.showerror("Error", f"An error occurred: {e}")
def on_progress(stream, chunk, bytes_remaining):
    total_size =stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded /total_size * 100
    per=str(int(percentage_of_compeletion))
    pPercentage.configure(text=per+"%")
    pPercentage.update()
    #update progress Bar
    progessBar.set(float(percentage_of_compeletion)/100)

#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk();
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
title= customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350,height=40,textvariable =url_var)
link.pack()
#Finished Downloading
finishlabel = customtkinter.CTkLabel(app ,text="")
finishlabel.pack()
#Progress Percentage
pPercentage  = customtkinter.CTkLabel(app,text ="0%")
pPercentage.pack()
progessBar = customtkinter.CTkProgressBar(app, width=400)
progessBar.set(0)
progessBar.pack(padx=10,pady=10)
# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=startDownload)
download_button.pack(padx=10,pady=10)

# Run app
app.mainloop()