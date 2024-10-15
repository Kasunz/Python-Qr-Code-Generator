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

# Run the application
root.mainloop()