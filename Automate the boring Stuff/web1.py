import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

address = address.replace(',','')
googleMapsURL = 'https://www.google.com/maps/place/'
webbrowser.open(googleMapsURL + address)

