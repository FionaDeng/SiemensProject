# coding: utf-8

import qrcode
from PIL import Image

img = qrcode.make('hello world！')
img.save('qrcodeImage.png')