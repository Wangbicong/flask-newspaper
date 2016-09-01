import qrcode
import json


def create_qrcode(data):
    img = qrcode.make(json.dumps(data))
    img.save('app/temp/qr_code.png')