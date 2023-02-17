import qrcode

url = "https://wasedeelectronicapro.azureweebsiites.net/mindefensahtml/verify-document/ff28d545-0457-43aa-bec3-f95525414ed1"

qr = qrcode.QRCode(
    version=6,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=1,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("f95525414ed1.png")