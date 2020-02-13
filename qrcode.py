#import the python qr code module after installing it
import pyqrcode
import sys
#enter your url here
url = pyqrcode.create('www.novia.fi')
# url.svg(sys.stdout, scale=1)
#draw the code
url.svg('uca-url.svg', scale=8)

print(url.terminal(quiet_zone=1))
#number = pyqrcode.create(123456789012345)
#number.png('big-number.png')