from cl213f import ebills

def main():
  try:
    with open("data/prog213f.dat", 'r') as f:
        bills=[]

        for line in f:
            kwh=int(line)
            if kwh == -999:
               break # will exit the loop right away
            
            kwhcost = ebills(kwh)
            bills.append(kwhcost) #append always adds to a list - pushes an item to the end of the list
        
        for lcv in range(len(bills)):
            bills[lcv].calc()
        
        for order in bills:
            print(order)
            print()

        # print(bills) - for the representation dunder method

  except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
  main()


# if -999 ignore it