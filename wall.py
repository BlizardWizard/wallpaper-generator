print("Nigga Penis 8====D")

from PIL import Image, ImageDraw, ImageEnhance
import random
import time
random.seed()

width = 1920
height = 1080

img = Image.new(mode="RGB", size=(width, height), color=(0, 0, 0))

enhancer = ImageEnhance.Contrast(img)
draw = ImageDraw.Draw(img)
j = width
cd = 0
line_width = width // 2

while True:
    for i in range(width):

        #color1 = random.randrange(1, 100)
        color1 = 50
        color2 = 0
        #color2 = random.randrange(1, 20)
        color3 = random.randrange(1, 100)
        line_width -= 1
        cd += random.randint(1,1)
        #draw.arc([(0, 0), (i, height)], 0, 360, fill=(color1, color2, color3), width=(axis_tilt))
        #draw.arc([(width - i, 0), (width, height)], 0, 360, fill=(color1, color2, color3), width=(axis_tilt))
        draw.line([(0, 0), (width, height)], fill=(color1 + cd, color2 + cd, 40), width=(line_width), joint="curve")
        #draw.line([(0, i), (width, i * 4 + axis_tilt)], fill=(color2, color1, color3), width=(abs(axis_tilt // 2)))
        #img = enhancer.enhance(1.1)

    img.show()
    #img.save("Image" + str(color1) + ".png")

    time.sleep(30)
