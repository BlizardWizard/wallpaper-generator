class Drawdata:
    xy1 = []
    xy2 = []
    fill = []
    line_width = []

    permiateScale = 100
    def permiateX(self):
        # permiates the x values of all datapoints in Drawdata object by permiateScale ammount 
        for i in range(len(self.xy1)):
            self.xy1[i] = (self.xy1[i][0] - self.permiateScale, self.xy1[i][1])
            self.xy2[i] = (self.xy2[i][0] - self.permiateScale, self.xy2[i][1])
    
    def reverseCycle(self, width):
        # pre: must be at end of cycle, or beginning or cycle
        # required pass width of screen
        # post: reverses direction of permiation
        # is void
        if self.xy2[len(self.xy2) - 1][0] <= width + self.permiateScale: # at end of cycle
            self.permiateScale *= -1
        elif self.xy1[0][0] >= 0: # at begining of new cycle
            self.permiateScale *= -1