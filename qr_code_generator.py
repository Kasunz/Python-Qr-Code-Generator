import os
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Ensure assets folder exits for save the qr codes
if not os.path.exists('assets'):
    os.makedirs('assets')

# Main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

# global variable for colors
foreground_color = "black"
background_color = "white"

# Function to generate qr codes
def generate_qr():
    global foreground_color, background_color

    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter data for the QR code")
        return

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill=foreground_color, back_color=background_color)
    filename = f"assets/qr_code_{len(os.listdir('assets')) + 1}.png"

    # Load and resize the image for display
    img = Image.open(filename)
    img = img.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    qr_label.config(image=img)
    qr_label.image = img

# function to choose foreground color
def choose_foreground():
    global foreground_color
    color = colorchooser.askcolor()[1]
    if color:
        foreground_color = color

# function to choose background color
def choose_background():
    global background_color
    color = colorchooser.askcolor()[1]
    if color:
        background_color = color




# Run the application
root.mainloop()