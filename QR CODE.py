import qrcode

url = input("enter the url :").strip()

path = "C:\\Users\\hp\\Desktop\\img.png"

qr = qrcode.QRCode()

qr.add_data(url)
img = qr.make_image()
img.save(path)

print("QR CODE GENERATED!!")