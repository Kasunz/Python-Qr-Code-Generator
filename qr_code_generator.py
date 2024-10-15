import os
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
import qrcode
from click import command
from pygments.styles.dracula import background
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

# function to select and decode a qr code from an image
def decode_qr():
    file_path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])

    if not file_path:
        return

    img = Image.open(file_path)

    # decode the qr code from the image
    result = decode(img)

    if result:
        messagebox.showinfo("QR Code Data", f"Decoded Data: {result[0].data.decode('utf-8')}")
    else:
        messagebox.showerror("Error", "No QR code found in the image.")

# Entry field for data
entry = tk.Entry(root, width=40)
entry.pack(pady=20)

# generate button
generate_button = tk.Button(root, text="Generate QR code", command=generate_qr)
generate_button.pack(pady=10)

# Label to show the QR code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# button to select color
foreground_button = tk.Button(root, text="Choose Foreground color", command=choose_foreground)
foreground_button.pack(pady=5)

background_button = tk.Button(root, text="Choose Foreground color", command=choose_background)
background_button.pack(pady=5)

# button to decode a qr code from an image
decode_button = tk.Button(root, text="Decode QR code from image", command=decode_qr)
decode_button.pack(pady=5)


# Run the application
root.mainloop()