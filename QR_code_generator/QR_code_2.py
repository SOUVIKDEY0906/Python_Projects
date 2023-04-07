import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,)

qr.add_data("https://twitter.com/SOUVIKDEY02")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="blue")
img.save("advance.png")
