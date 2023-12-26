class rectangle:
    # constructor
    def __init__(self,length, width):
        self.length = length
        self.width = width
        self.area = 0
        self.perem = 0

    def calc(self):
        self.area = self.length * self.width
        self.perem = self.length*2 + self.width*2

    def getarea(self):
        return self.area
    
    def getperem(self):
        return self.perem
    

#prog52acl