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


while True:
    for i in range(width):
        random.seed()
        line_width = random.randrange(1, 20)
        color1 = random.randrange(1, 40)
        color2 = random.randrange(1, 2)
        color3 = random.randrange(1, 60)
        cd = random.randint(-100,100)
        #draw.arc([(0, 0), (i, height)], 0, 360, fill=(color1, color2, color3), width=(line_width))
        #draw.arc([(width - i, 0), (width, height)], 0, 360, fill=(color1, color2, color3), width=(line_width))
        #draw.line([(0, 0), (width, height)], fill=(color1 + cd, color2 + cd, 40), width=(line_width), joint="curve")
        draw.line([(0, i), (width, i + cd )], fill=(color1, color2, color3), width=line_width)
        #img = enhancer.enhance(1.1)


    img.save("image.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"\image.png" , 0)

    time.sleep(2)
