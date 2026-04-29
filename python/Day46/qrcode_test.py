import qrcode
img=qrcode.make("https://www.youtube.com/@codewithharry")
img.save("myqr.png")
print("QR code saved as myqr.png")