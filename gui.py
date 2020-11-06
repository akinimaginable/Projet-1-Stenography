import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from typing import Optional

from PIL import Image, ImageTk

from main import encrypt, decrypt


# Commands
def open_file_command():
    file = tk.filedialog.askopenfilename(initialdir="~/", title="Choose an image file",
                                         filetypes=(('PNG files', '.png'), ('JPG files', '.jpg'), ("All files", ".*")))
    if file != "":
        global image_file, image
        image_file = str(file)
        image = open_image(image_file)


def about_command():
    tk.messagebox.showinfo(title="About", message="NSI 2020/2021")


def save_file_command(image: Image.Image):
    image.save(image_file, "png")
    tk.messagebox.showinfo("Info", "Image saved")


def quit_command():
    root.destroy()


def open_image(image_file) -> Optional[Image.Image]:
    """
    Opens an image and displays it in the label
    image_file: path of the image
    """
    try:
        image = Image.open(image_file)
        if image.size[0] > 800 or image.size[1] > 450:
            image = image.resize((800, 450), Image.LANCZOS)

        photo = ImageTk.PhotoImage(image)
        label_img.config(image=photo)
        label_img.image = photo
        return image

    except FileNotFoundError:
        print("Image not found")

    return None


def continue_command(image, radio_variable):
    """
    Encrypts or decrypts the image
    radio_variable: chosen option
    1 encryption; 2 decryption
    output: if encryption: image; if decryption: message
    """
    if radio_variable.get() == 1:  # Encryption
        if image is not None:
            text = message.get("1.0", "end")
            image = encrypt(text, image)
            if image is not None:
                image.save("007.png", "png")
                tk.messagebox.showinfo("Info", "Image saved successfully")
            else:
                tk.messagebox.showerror(title="Error",
                                        message="The message is too long to be steganographed in the image")
    elif radio_variable.get() == 2:  # Decryption
        if image is not None:
            text = decrypt(image)
            change_message_text(text)


def mode_encryption():
    """
    Encryption mode: reactivates the Text, disables readonly mode
    """
    message.configure(state="normal")  # to be able to write in the text, disable readonly mode


def mode_decryption():
    """
    Decryption mode: activates readonly mode on the Text
    """
    message.configure(state='normal')  # to be able to write in the text, disable readonly mode
    message.delete(1.0, "end")  # delete the text
    message.configure(state='disabled')  # re-enable readonly mode


def change_message_text(text):
    """
    Changes the message of the Text in decryption mode
    text: text to display in the TEXT message
    """
    message.configure(state='normal')  # to be able to write in the text, disable readonly mode
    message.delete(1.0, "end")  # delete the text
    message.insert(1.0, text)  # write the text
    message.configure(state='disabled')  # re-enable readonly mode


def get_menubar(root) -> tk.Menu:
    """
    Creates the window menu and assigns functions to it
    root: graphical window
    output: Menu bar
    """
    menu_bar = tk.Menu(root)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file_command)
    file_menu.add_command(label="Save", command=lambda: save_file_command(image))
    file_menu.add_command(label="Quit", command=quit_command)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=about_command)

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    return menu_bar


if __name__ == "__main__":
    image_file: str = "tests/default.png"

    # Window creation
    root = tk.Tk()  # create a window
    root.title("Secret Agent")  # window title
    radioVariable = tk.IntVar()

    # Create a Label
    presentation = tk.Label(root, text="Secret Agent: Encrypt or decrypt an image")  # create the label
    # place the label in the window at position 0,0 with size 2,1
    presentation.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Create the label containing the image
    label_img = tk.Label(root)  # create the label
    # place the label in the window at position 0,1 with size 2,2
    label_img.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="nsew")
    image = open_image(image_file)

    # Menu bar
    Menubar = get_menubar(root)  # Create the menu bar
    root.config(menu=Menubar)

    # Create a radio button
    b_radio_1 = tk.Radiobutton(root, variable=radioVariable, text="Encrypt", value=1, indicatoron=False)
    # place radio button 1 in the window at position 3,0 with size 1,1
    b_radio_1.grid(row=3, column=0, sticky="nsew")
    b_radio_2 = tk.Radiobutton(root, variable=radioVariable, text="Decrypt", value=2, indicatoron=False)
    # place radio button 2 in the window at position 3,1 with size 1,1
    b_radio_2.grid(row=3, column=1, sticky="nsew")
    b_radio_1.invoke()

    # Create a Text Message
    message = tk.Text(root)
    # place the Text message in the window at position 4,0 with size 2,1
    message.grid(row=4, column=0, columnspan=2, sticky="ew")

    # Radio
    b_radio_1["command"] = lambda: mode_encryption()
    b_radio_2["command"] = lambda: mode_decryption()

    # Create a Continue button
    continue_button = tk.Button(root, text="Continue")
    # Place the continue button in the window at position 4,0 with size 2,1
    continue_button.grid(row=6, column=0, columnspan=2, sticky="nsew")
    continue_button["command"] = lambda: continue_command(image, radioVariable)  # Assign a command to the button

    # Window adaptation
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(4, weight=1)

    root.mainloop()  # display the window
