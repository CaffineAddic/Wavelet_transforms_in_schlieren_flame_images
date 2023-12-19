import tkinter as tk
from tkinter import filedialog
import os
import cv2
import numpy as np

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        process_folder(folder_path)

def process_folder(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            image_path = os.path.join(folder_path, file)
            image = cv2.imread(image_path)
            if image is not None:
                channels = cv2.split(image)
                for i, channel in enumerate(channels):
                    channel_path = os.path.join(folder_path, f"{os.path.splitext(file)[0]}_{i}.npy")
                    np.save(channel_path, channel)
        else:
            print(f"Ignoring {file} as it is not a supported image format.")

# Create a new instance of Tkinter
window = tk.Tk()

# Set the window title
window.title("Image Channel Extraction")

# Create a button widget to select the folder
select_button = tk.Button(window, text="Select Folder", command=select_folder)

# Pack the button widget to display it
select_button.pack()

# Start the Tkinter event loop
window.mainloop()