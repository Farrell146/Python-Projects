class Animal:
    def __init__(self, fn, ln):
        self._first=fn
        self._last=ln
        #setting these as private by using only one underscore after self "_first"

    def getName(self):
        return self._first+" "+self._last
    
class Hicca(Animal):
    def __init__(self, fn, ln, fur):
        super().__init__(fn,ln)
        self.fur=fur
    
class Wallie(Animal):
    def __init__(self, fn, ln, steps):
        super().__init__(fn,ln)
        self.steps=steps

class Beeper(Animal):
    def __init__(self, fn, ln, eword):
        super().__init__(fn,ln)
        self.eword=eword
