import qrcode


def create_qrcode(data):
    img = qrcode.make(str(data))
    img.save('app/temp/qr_code.png')