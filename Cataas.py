from cProfile import label
from tkinter import *
from tkinter import Label

import requests
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title('Cats!')
window.geometry('600x400')

label = Label()
label.pack

url = 'https://cataas.com/cat'
img = load.image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
