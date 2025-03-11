import qrcode

with open("QN.py", "rb") as file:
    content = file.read()

img = qrcode.make(content)
img.save("QR_CODE.png")
print("QR CODE GENERATED!")
