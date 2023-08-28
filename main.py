from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog

uploaded_img = PIL.Image.open("00633_oceanhope_672x420.jpg")


def upload_file():
    global img, img_orig, img_btn
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img_orig = PIL.Image.open(filename)

    img_resized = img_orig.resize((300, 200))
    img = ImageTk.PhotoImage(img_resized)
    img_btn = Button(window, image=img)  # using Button
    img_btn.grid(row=2, column=1, columnspan=2)

    download_btn = Button(window, text="Download Full Image", width=20, command=img_orig.show)
    download_btn.grid(row=3, column=1)


def add_watermark():
    global photo_img
    watermark = PIL.Image.open("pngfind.com-watermark-png-791974.png")
    img_size = uploaded_img.size
    center_position = (
        (img_size[0]) // 3,
        (img_size[1]) // 3,
    )
    img_orig.paste(watermark, center_position, mask=watermark)
    img_resized = img_orig.resize((300, 200))
    photo_img = ImageTk.PhotoImage(img_resized)
    img_btn.configure(image=photo_img)


window = Tk()
window.geometry("300x300")
window.title("Watermark Template")
upload_btn = Button(window, text="Upload Picture", width=20, command=upload_file)
upload_btn.grid(row=1, column=1)
watermark_btn = Button(window, text="Add Watermark", width=20, command=add_watermark)
watermark_btn.grid(row=1, column=2)

window.mainloop()
