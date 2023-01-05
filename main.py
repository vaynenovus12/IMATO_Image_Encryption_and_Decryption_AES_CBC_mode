import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename

from Crypto.Util.Padding import pad, unpad
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
from Crypto.Cipher import AES


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    splash_root.geometry('%dx%d+%d+%d' % (width, height, x, y))


# Splash screen
splash_root = Tk()
center_window(900, 600)
# Hide the title bar
splash_root.overrideredirect(True)
splash_root.columnconfigure(0, weight=3)

app_name = Label(text="IMATO", font=("Modern Warfare", 29))
app_name.grid(row=1)

dev_team_label = Label(text="Developed by Team Inventor", font=("Modern Warfare", 16))
dev_team_label.grid(row=2)

open_gif = Image.open("resources/loading_anim.gif")
frames = open_gif.n_frames
imageObj = [PhotoImage(file="resources/loading_anim.gif", format=f"gif -index {i}") for i in range(frames)]

showAnimation = None


def animation(count=0):
    global showAnimation
    newImage = imageObj[count]

    loading_label.configure(image=newImage)
    count += 1
    if count == frames:
        count = 0
    showAnimation = splash_root.after(50, lambda: animation(count))


loading_label = Label(splash_root, image="")
loading_label.grid(row=3)
animation(count=0)


# Main window
def main_window():
    splash_root.destroy()

    gui = Tk(className='Imato - Image Encryption and Decryption App')

    def exit_app():
        gui.destroy()

    # Maps the RGB
    def convert_to_rgb(data):
        r, g, b = tuple(map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
        pixels = tuple(zip(r, g, b))
        return pixels

    # CBC
    def aes_cbc_encrypt(aes_cbc_key, data, mode=AES.MODE_CBC):
        iv_enc = "A" * 16  # We'll manually set the initialization vector to simplify things
        encrypt_aes = AES.new(aes_cbc_key.encode("utf8"), mode, iv_enc.encode("utf8"))
        new_data = encrypt_aes.encrypt(data)
        return new_data

    # CBC
    def aes_cbc_decrypt(aes_cbc_key, data, mode=AES.MODE_CBC):
        iv_dec = "A" * 16  # We'll manually set the initialization vector to simplify things
        decrypt_aes = AES.new(aes_cbc_key.encode("utf8"), mode, iv_dec.encode("utf8"))
        new_data = decrypt_aes.decrypt(data)
        return new_data

    def process_img_encrypt():
        key_encrypt = key_field.get()
        filename = askopenfilename()

        # Opens image and converts it to RGB format for PIL
        image1 = Image.open(filename)
        data = image1.convert("RGB").tobytes()

        # Since we will pad the data to satisfy AES's multiple-of-16 requirement, we will store the original data length
        # and "unpad" it later.
        original = len(data)

        # Encrypts using AES mode (CBC)
        new = convert_to_rgb(aes_cbc_encrypt(key_encrypt, pad(data, AES.block_size))[:original])

        # Create a new PIL Image object and save the old image data into the new image.
        im2 = Image.new("RGBA", image1.size)

        im2.putdata(new)

        # Save image
        im2.save("encrypted_img" + "." + "PNG", "PNG")

        if image1.width > 600 and image1.height > 600:
            resized_image = image1.resize((800, 600), Image.LANCZOS)
        elif image1.width > 600:
            resized_image = image1.resize((800, image1.height), Image.LANCZOS)
        elif image1.height > 600:
            resized_image = image1.resize((image1.width, 600), Image.LANCZOS)
        else:
            resized_image = image1
        img = ImageTk.PhotoImage(resized_image)
        imageLabel.image = img
        imageLabel.configure(image=img, width=800, height=600)
        imageLabel.grid(column=0, row=3, sticky=tkinter.W)
        print(filename)

        result_image = Image.open("encrypted_img.PNG")
        if result_image.width > 600 and result_image.height > 600:
            resized_image = result_image.resize((800, 600), Image.LANCZOS)
        elif result_image.width > 600:
            resized_image = result_image.resize((800, result_image.height), Image.LANCZOS)
        elif result_image.height > 600:
            resized_image = result_image.resize((result_image.width, 600), Image.LANCZOS)
        else:
            resized_image = result_image
        img_res = ImageTk.PhotoImage(resized_image)
        imageLabel.image = img_res
        resultImgLabel.configure(image=img_res, width=800, height=600)
        resultImgLabel.grid(column=0, row=3, sticky=tkinter.E)
        messagebox.showinfo("Info", "Encrypted image has been saved.")
        image1.close()

    def process_img_decrypt():
        key_decrypt = key_field.get()

        # Opens image and converts it to RGB format for PIL
        image2 = Image.open("encrypted_img.PNG")
        data = image2.convert("RGB").tobytes()

        # Since we will unpad the data to satisfy AES's multiple-of-16 requirement, we will store the original data
        # length
        original = len(data)

        # Decrypt using AES mode (CBC)
        new = convert_to_rgb(aes_cbc_decrypt(key_decrypt, pad(data, AES.block_size))[:original])

        # Create a new PIL Image object and save the old image data into the new image.
        im2 = Image.new("RGBA", image2.size)
        im2.putdata(new)

        # Save image
        im2.save("decrypted_img" + "." + "PNG", "PNG")

        if image2.width > 600 and image2.height > 600:
            resized_image = image2.resize((800, 600), Image.LANCZOS)
        elif image2.width > 600:
            resized_image = image2.resize((800, image2.height), Image.LANCZOS)
        elif image2.height > 600:
            resized_image = image2.resize((image2.width, 600), Image.LANCZOS)
        else:
            resized_image = image2
        img2 = ImageTk.PhotoImage(resized_image)
        imageLabel.image = img2
        imageLabel.configure(image=img2, width=800, height=600)
        imageLabel.grid(column=0, row=3, sticky=tkinter.W)

        result_image = Image.open("decrypted_img.PNG")
        if result_image.width > 600 and result_image.height > 600:
            resized_image = result_image.resize((800, 600), Image.LANCZOS)
        elif result_image.width > 600:
            resized_image = result_image.resize((800, result_image.height), Image.LANCZOS)
        elif result_image.height > 600:
            resized_image = result_image.resize((result_image.width, 600), Image.LANCZOS)
        else:
            resized_image = result_image
        imgres = ImageTk.PhotoImage(resized_image)
        imageLabel.image = imgres
        resultImgLabel.configure(image=imgres, width=800, height=600)
        resultImgLabel.grid(column=0, row=3, sticky=tkinter.E)
        messagebox.showinfo("Info", "Decrypted image has been saved.")
        image2.close()

    gui.geometry("1920x1080")

    gui.columnconfigure(0, weight=6)

    gui['bg'] = "#000000"

    gui.attributes('-fullscreen', True)

    header = Label(gui, text="IMATO", font=("Modern Warfare", 40), foreground="#f1f1f1", background="#000000")
    subheader = Label(gui, text="Image Encryption and Decryption", font=("Modern Warfare", 25), foreground="#78bf2b",
                      background="#000000")
    exitBtn = Button(gui, text="Exit", command=exit_app, background="#60972f", highlightthickness=0,
                     bd=0, foreground="#fffffe", font=("Modern Warfare", 20))

    imageLabel = Label(gui, width=80, height=30, background="#000000", highlightbackground='white',
                       highlightthickness=2)
    resultImgLabel = Label(gui, width=80, height=30, background="#000000", highlightbackground='white',
                           highlightthickness=2)

    uploadBtn = Button(gui, text="Encrypt", command=process_img_encrypt, background="#ffffff", highlightthickness=0,
                       bd=0,
                       foreground="#950815", font=("Modern Warfare", 20))
    buttonBorder = tkinter.Frame(gui, highlightbackground='white', highlightthickness=2, bd=0)
    decryptBtn = Button(buttonBorder, text="Decrypt", command=process_img_decrypt, background="#000000",
                        highlightthickness=0, bd=0,
                        foreground="#fffffe",
                        font=("Modern Warfare", 20))
    key_field = Entry(gui, background="#58595b", foreground="#fffffe",
                      font=("Modern Warfare", 29), width=35, borderwidth=0)
    key_field.insert(0, "Enter your key")

    exitBtn.grid(column=0, row=0, sticky=tkinter.NE, padx=15, pady=15)
    header.grid(column=0, row=1, sticky=tkinter.EW)
    subheader.grid(column=0, row=2, sticky=tkinter.EW)

    imageLabel.grid(column=0, row=3, sticky=tkinter.W, padx=115, pady=25)
    resultImgLabel.grid(column=0, row=3, sticky=tkinter.E, padx=115, pady=25)

    uploadBtn.grid(column=0, row=4, sticky=tkinter.SW, padx=145)
    decryptBtn.grid(column=0, row=4, sticky=tkinter.SE)
    buttonBorder.grid(column=0, row=4, sticky=tkinter.SE, padx=145)
    key_field.grid(column=0, row=4, sticky=tkinter.S, padx=145, ipadx=20, ipady=5)


splash_root.after(3000, main_window)
mainloop()
