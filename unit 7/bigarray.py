from bigarrayhelper import Cat

def main():
  try:
    with open("data/bigarraylist.dat", 'r') as f:
        catil=[]
        catlist=[]

        for line in f:
            catil.append(line)
            
        catamt=int(catil[0])
        catscrape=1
        for c in range(0,catamt,1):            
            catuple=str(catil[catscrape]).strip(),float(catil[catscrape+1]),int(catil[catscrape+2]),float(catil[catscrape+3])
            newcat=Cat(*catuple)
            catlist.append(newcat)

            catscrape+=4
        
        def getList(cat):
            return f"{cat.name}\t{cat.weight}\t{cat.age}\t{cat.cost}"

        def getName(cat):
            return cat.name
    
        def getWeight(cat):
            return cat.weight
    
        def getAge(cat):
            return cat.age
    
        def getCost(cat):
            return cat.cost

        #1 Print out all the cats (there is no toString() available)
        print("All the cats:")
        print("Name\tWeight\tAge\tCost")
        for lcv in range(len(catlist)):
            print(str(getList(catlist[lcv])))
        print()
        
        #2 Print the name of the 3rd cat.
        print("3rd Cat:", str(getName(catlist[2])))
        print()
        
        #3 The last cat has gained 10 pounds. Update the weight on the object. Print the new weight.
        newweight = getName(catlist[-1]), getWeight(catlist[-1])+10, getAge(catlist[-1]), getCost(catlist[-1])
        catlist[-1] = Cat(*newweight)
        print("Updated weight is:",getWeight(catlist[-1]))
        print()
        
        #4 The cat named Rascal died. Find that cat and remove it from the list
        for riprascal in range(len(catlist)):
            if getName(catlist[riprascal]) == "Rascal":
                catlist.remove(catlist[riprascal])
                break
        
        #5 A new kitten was brought in (Angel, 3.6, 1, 25.99).  Insert it into the 2nd cell.
        newcat="Angel", 3.6, 1, 25.99
        catlist.insert(1,Cat(*newcat))
        
        #6 A new geriatric cat was found (Gimpy, 14.3, 10,  29.99). Put him on the list. 
        newcat="Gimpy", 14.3, 10, 29.99
        catlist.append(Cat(*newcat))
        
        #7 Print the updated list with a for-each loop
        print("Updated list:")
        print("Name\tWeight\tAge\tCost")
        for x in range(len(catlist)):
           print(getList(catlist[x]))
        print()
        
        #8 Replace the 3rd cat with (Sugar, 23.6, 7, 33.25) put the removed cat at the end of the list.
        bookcat=catlist[2]
        catlist[2]=Cat("Sugar", 23.6, 7, 33.25)
        catlist.append(bookcat)
        
        #9 Switch the 2nd and 4th cats.
        bookcat=catlist[1]
        catlist[1]=catlist[3]
        catlist[3]=bookcat

        #10 Print the names of the cats on the list.
        print("Current Names:")
        names=[]
        for y in range(len(catlist)):
           names.append(getName(catlist[y]))
        a=" ".join(names)
        print(a)
        print()
        
        #11 Remove all cats under $26. Print the costs of each cat remaining on the list.
        void=Cat("Void",0,0,0)
        voidcnt=0
        for cheapcat in range(len(catlist)):
           if getCost(catlist[cheapcat]) < 26.00:
              catlist[cheapcat]=void
              voidcnt+=1
        
        check=0
        while voidcnt>0:
            if catlist[check]==void:
                catlist.remove(catlist[check])
                voidcnt-=1
            check+=1

        print("Cats costing $26 or more actually cost:")
        Costs=[]
        for k in range(len(catlist)):
           Costs.append(getCost(catlist[k]))
        a="".join(str(Costs))
        print(a)
        print()
        
        #12 All cats heavier than 15 pounds need to go on a diet <--  no for-each this time.
        fat=[]
        for eat in range(len(catlist)):
           if getWeight(catlist[eat])>15:
              fat.append(getName(catlist[eat]))
        print("Fat Cats:")
        a=" ".join(fat)
        print(a)
        
  except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
  main()

"""
All the cats:
Name    Weight  Age     Cost
Inky    15.69   2       35.79
Panda   14.3    6       15.03
Rascal  21.1    21      0.0
Blacky  13.99   3       26.89
Taffy   24.5    10      56.89
Toby    17.2    10      37.57

3rd Cat: Rascal

Updated weight is: 27.2

Updated list:
Name    Weight  Age     Cost
Inky    15.69   2       35.79
Angel   3.6     1       25.99
Panda   14.3    6       15.03
Blacky  13.99   3       26.89
Taffy   24.5    10      56.89
Toby    27.2    10      37.57
Gimpy   14.3    10      29.99

Current Names:
Inky Blacky Sugar Angel Taffy Toby Gimpy Panda 

Cats costing $26 or more actually cost:        
[35.79, 26.89, 33.25, 56.89, 37.57, 29.99]     

Fat Cats:
Inky Sugar Taffy Toby
"""