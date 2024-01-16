from cl701p import *

def main():
  try:
    animals=[]
    with open("data/prog701g.dat", 'r') as f:
        num=int(f.readline())
        while num != 99:
            fn = f.readline()
            ln = f.readline()
            if num == 1:
                fur = float(f.readline())
                p = Hicca(fn,ln,fur)
                animals.append(p)
            elif num == 2:
                steps = int(f.readline())
                p = Wallie(fn,ln,steps)
                animals.append(p)
            elif num == 3:
                eword = f.readline().strip()
                p = Beeper(fn,ln,eword)
                animals.append(p)
            num=int(f.readline())
        
        tot = 0.0
        cnt = 0
        totsteps = 0
        stepavg = 0
        avgword = 0.0
        wordcnt = 0
        garb=""

        for animal in animals:
            if isinstance(animal, Hicca):
                tot += animal.fur
                cnt += 1
            if isinstance(animal, Wallie):
               totsteps += animal.steps
               stepavg+=1
            if isinstance(animal, Beeper):
                wordcnt+=1
                eword = animal.eword
                avgword+=len(eword)
                garb+=eword
                

                
            
        print("Average value of Hicca fur:", round(tot/cnt,2))
        print("Average number of steps taken by the Wallies:", round(totsteps/stepavg,2))
        print("Average size of Beepers words:", round(avgword/wordcnt,2))

        c=sorted(garb)
        e=0
        letter=""

        list=[]

        for i in range(len(c)):
            if letter != c[i]:
                if e<c.count(c[i]) or e==c.count(c[i]):
                    e=c.count(c[i])
                    letter=c[i]
                    list.append(letter)
        a=" ".join(list)

        print("The most common letters in all the Beeper's words:", a)

        
        
  except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
  main()

"""
Average value of Hicca fur: 3.06
Average number of steps taken by the Wallies: 63.2
Average size of Beepers words: 7.25
The most common letters in all the Beeper's words: a e
"""