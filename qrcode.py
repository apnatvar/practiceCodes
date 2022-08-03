import pyqrcode
import png
from pyqrcode import QRCode
from PySimpleGUI import *

layout = [[Text('Enter website', key='__INPUT__'),InputText(), Button('Generate QR Code')]]
window = Window('QR Code Generator', layout, resizable=True)
while True:
    event, values = window.read()
    if event == 'Generate QR Code':
        s = values[0]
        print(s)
        url = pyqrcode.create(s)
        url.svg(f"{s[1:3]}.svg",scale=8)
        url.png(f'{s[1:3]}.png',scale=6)
