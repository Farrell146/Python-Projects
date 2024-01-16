class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sayHi(self):
        print("Hi")

class cat(animal):
    def __init__(self,name,age,sound):
        #animal.__init__(name, age)
        super().__init__(name, age)
        self.sound=sound
    
    def saySound(self):
        print("Meow")

catt = cat("Billy", 5, "Meow")
catt.sayHi()
catt.saySound()