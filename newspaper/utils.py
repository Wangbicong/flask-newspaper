# -*- coding:utf-8 -*-
import os
import qrcode


def generate_qrcode(data):
    img = qrcode.make(data)
    cur_path = os.path.abspath('.')
    img.save(cur_path+'/static/qrcode.jpg')

if __name__ == '__main__':
    generate_qrcode('H')