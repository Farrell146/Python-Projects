class Cat:
    def __init__(self, catuple):
        self.name,self.weight,self.age,self.cost=catuple
        # self.name = name
        # self.weight = weight
        # self.age = age
        # self.cost = cost
    
    def getInfo(self):
        return self.name,self.weight,self.age,self.cost
    
    def getList(self):
        return f"{self.name}\t{self.weight}\t{self.age}\t{self.cost}"
    
    def getName(self):
        return self.name
    
    def getWeight(self):
        return self.weight
    
    def getAge(self):
        return self.age
    
    def getCost(self):
        return self.cost