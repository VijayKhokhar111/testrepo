import qrcode

qr_img = qrcode.make("hello")

qr_img.save("qr_img.jpg")
