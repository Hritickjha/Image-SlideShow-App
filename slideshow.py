from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root= tk.Tk()
root.title("Image slideshow viewer")

# List of Image path
image_paths = [
    r"C:\Users\97798\OneDrive\Pictures\Camera Roll\WIN_20231205_08_08_25_Pro.jpg",
    r"C:\Users\97798\OneDrive\Pictures\Camera Roll\WIN_20231205_08_08_35_Pro.jpg",
    r"C:\Users\97798\OneDrive\Pictures\Camera Roll\WIN_20231205_08_08_44_Pro.jpg",
]

#Resize the images to 1080*1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images =[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        root.update()
        time.sleep(3)  
slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='play slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()
        
                             