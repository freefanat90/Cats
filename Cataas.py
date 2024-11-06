from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None

def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def exit_win():
    window.destroy()

window = Tk()
window.title('Cats!')
window.geometry('600x520')

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

main_bar = Menu(window)
window.config(menu=main_bar)

file_menu = Menu(main_bar, tearoff=0)
main_bar.add_cascade(label='Файл', menu=file_menu)

file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выйти', command=exit_win)

url = 'https://cataas.com/cat'

window.mainloop()
