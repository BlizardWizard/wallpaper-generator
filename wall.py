print("⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿")
print("⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿")
print("⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻")
print("⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄")
print("⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄")

from PIL import Image, ImageDraw, ImageEnhance
import random
import time
import ctypes
import os
from Drawdata import Drawdata

random.seed()

width = 1920
height = 1080

img = Image.new(mode="RGB", size=(width, height), color=(0, 0, 0))

enhancer = ImageEnhance.Contrast(img)
draw = ImageDraw.Draw(img)
j = width
cd = 0

data = Drawdata()
for i in range(width):
    cd = random.randint(-100,100)
    data.xy1.append((0, i))
    data.xy2.append((width*10, i + cd))
    data.fill.append((random.randrange(1, 40), random.randrange(1, 2), random.randrange(1, 60)))
    data.line_width.append(random.randrange(1, 20))

while True:
    for i in range(width):
        
        #draw.arc([(0, 0), (i, height)], 0, 360, fill=(color1, color2, color3), width=(line_width))
        #draw.arc([(width - i, 0), (width, height)], 0, 360, fill=(color1, color2, color3), width=(line_width))
        #draw.line([(0, 0), (width, height)], fill=(color1 + cd, color2 + cd, 40), width=(line_width), joint="curve")
        #img = enhancer.enhance(1.1)

        draw.line([data.xy1[i], data.xy2[i]], fill=data.fill[i], width=data.line_width[i])

    data.permiateX()
    data.reverseCycle(width)
    img.save("image.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"\image.png" , 0)

    time.sleep(0.05)
