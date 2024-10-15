import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqrcode = qrcode.make("Hello!")
myqrcode.save("myqrcode.png", scale=8)

decode_msg = decode(Image.open("myqrcode.png"))
print(decode_msg[0].data.decode("ascii"))