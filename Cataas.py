from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

def loade_image():
    try:
        response = requests.get(url)
        response.rise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None

window = Tk()
window.title('Cats!')
window.geometry('600x400')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
