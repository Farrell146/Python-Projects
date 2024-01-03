from cl213b import qtyordering

def main():
  try:
    with open("data/prog213b.dat", 'r') as f:
        orders=[]

        for line in f:
            qty=int(line)

            qtyorder= qtyordering(qty)
            orders.append(qtyorder) #append always adds to a list - pushes an item to the end of the list
        
        for lcv in range(len(orders)):
            orders[lcv].calc()
        
        for order in orders:
            print(order)
            print()

        # print(orders) - for the representation dunder method

  except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
  main()







"""
test = qtyordering(5) #this calls __init__
test.calc() #this is running the calc function in the helper class
print(test) #this calls __str__ (will hunt for a str)  || can also be called as print(str(test))
"""