import qrcode
from PIL import Image
url= "https://www.bioxsystems.com/"

myqr1= qrcode.make(url)
myqr1.save("myqr1.png")
img = Image.open("myqr1.png")
img.show()
img.save("Biox Systems.png")