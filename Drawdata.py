from random import randrange
from time import time

class Drawdata:
    xy1 = []
    xy2 = []
    fill = []
    line_width = []
    drawtype = 0
    def __init__(self):
        self.birth = time()

    permiateScale = 100
    def permiateX(self):
        # permiates the x values of all datapoints in Drawdata object by permiateScale ammount 
        for i in range(len(self.xy1)):
            self.xy1[i] = (self.xy1[i][0] - self.permiateScale, self.xy1[i][1])
            self.xy2[i] = (self.xy2[i][0] - self.permiateScale, self.xy2[i][1])
    
    def age(self):
        return time() - self.birth

    def randomizeY(self):
        randScale = 2
        for i in range(len(self.xy1)):
            rand1 = randrange(-randScale, randScale)
            self.xy1[i] = (self.xy1[i][0], self.xy1[i][1] + rand1)
            rand2 = randrange(-randScale, randScale)
            self.xy2[i] = (self.xy2[i][0], self.xy2[i][1] + rand2)