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


width = 1920
height = 1080

img = Image.new(mode="RGB", size=(width, height), color=(0, 0, 0))

enhancer = ImageEnhance.Contrast(img)
draw = ImageDraw.Draw(img)
j = width
cd = 0
line_width = random.randrange(1, 100)

while True:
    for i in range(width):
        random.seed()
        color1 = random.randrange(1, 200)
        color2 = random.randrange(1, 200)
        color3 = random.randrange(1, 200)
        cd += random.randint(1,1)
        draw.arc([(0, 0), (i, height)], 0, 360, fill=(color1, color2, color3), width=(line_width))
        draw.arc([(width - i, 0), (width, height)], 0, 360, fill=(color1, color2, color3), width=(line_width))
        #draw.line([(0, 0), (width, height)], fill=(color1 + cd, color2 + cd, 40), width=(line_width), joint="curve")
        #draw.line([(0, i), (width, i * 4 + axis_tilt)], fill=(color2, color1, color3), width=(abs(axis_tilt // 2)))
        #img = enhancer.enhance(1.1)


    img.save("image.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"\image.png" , 0)

    time.sleep(5)
