# Python QR Code Generator

This project provides a QR code generator with a GUI built using Python's `Tkinter` library. The application allows users to create QR codes from custom input, customize QR code colors, and decode QR codes from images.

## Features

- **GUI (Graphical User Interface)** using Tkinter.
- Ability to:
  - Enter custom text or URLs for the QR code.
  - Customize QR code colors (foreground and background).
  - Save QR codes with unique filenames (prevents overwriting).
  - Generate multiple QR codes without overwriting previous ones.
  - Select an image from your system to decode a QR code.

## Installation

Make sure you have the following Python libraries installed:

```bash
pip install qrcode Pillow pyzbar
```

## Project Structure

- **`qr_code_generator.py`**: The main Python script that contains the logic for the QR code generator.
- **`assets/`**: Folder where all generated QR codes are saved.

## Usage

### Generate a QR Code:

- Enter text like: "Hello! How are you?"
- Click on "Generate QR code" to see the result.

### Change the QR Code Colors:

- Select your desired foreground and background colors using the color chooser dialogs before generating the QR code.

### Decode a QR Code:

- Choose a PNG file containing a QR code using the "Decode QR code from image" button. The decoded data will appear in a dialog box.



