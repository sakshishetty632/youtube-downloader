# PythonTube-Downloader

YouTube Downloader is a simple Python application that allows users to download YouTube videos in the highest resolution available. The application uses the tkinter library for the graphical user interface, the pytube library for downloading YouTube videos, and a custom customtkinter library for UI customization.

## Features
Download YouTube videos in the highest resolution available.
Real-time progress updates during the download process.
User-friendly interface with customization options.
## Requirements
Python 3.x
tkinter library (usually included in standard Python installations)
pytube library (install via pip install pytube3)
customtkinter library (if necessary; make sure to have it compatible with your Python version)
## How to Use
1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using pip if you don't have them already:
```
pip install pytube3
```
4. Download the customtkinter library and make sure it is accessible to the application.
5.  Run the youtube_downloader.py script using Python:
```
python youtube_downloader.py
```
5. The application window will open, prompting you to insert a YouTube link.
6. Copy and paste the YouTube video link into the input field and click the "Download" button.
7. The video download will begin, and you will see real-time progress updates on the progress bar and percentage label.
8. Once the download is complete, the "Downloaded" message will be displayed.
9. You can download another video by repeating steps 5 to 8.
10. If any errors occur during the download process, an error message will be displayed, and you can try again.

## Customization
The application uses the customtkinter library for customizing the appearance. If you want to change the color theme or appearance mode, you can modify the customtkinter.set_appearance_mode() and customtkinter.set_default_color_theme() functions in the script.

## Acknowledgments
The pytube library by Nick Ficano: https://pytube.io/
The tkinter library for the GUI framework.
The customtkinter library (if applicable) for UI customization.

## Author
Sakshi Shetty

GitHub: sakshishetty632
