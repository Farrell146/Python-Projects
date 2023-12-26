class circle:
    def __init__(self,radius):
        self.radius=radius
        self.area=0
        self.cir=0

    def calc(self):
        from math import pi
        self.area = pi*self.radius**2
        self.cir = 2 * pi * self.radius

    def getarea(self):
        return round(self.area,3)
    
    def getcir(self):
        return round(self.cir,3)