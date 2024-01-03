class ebills:
    def __init__(self,kwh):
        self.kwh=kwh
        self.cost=0
    
    def calc(self):
        if self.kwh <= 2000:
            self.cost=self.kwh*.07
        elif self.kwh <= 10000:
            self.cost=140+((self.kwh-2000)*.05)
        elif self.kwh > 10000:
            self.cost=540+((self.kwh-10000)*.04)

    def __str__(self):
        return f"The cost of {self.kwh} KWH is: ${self.cost:.2f}"