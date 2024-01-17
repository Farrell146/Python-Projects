from cl702q import *

def main():
  try:
    vehicles=[]
    with open("data/prog702q.dat", 'r') as f:
        lines=f.readlines()
        for lcv in range(0,len(lines),4):
            car=int(lines[lcv])
            name=lines[lcv+1]
            tires=int(lcv+2)
            if car == 1:
                worth=int(lines[lcv+3])
                c = Car(name,tires,worth)
                vehicles.append(c)
            elif car == 2:
                miles=int(lines[lcv+3])
                c = Truck(name,tires,miles)
                vehicles.append(c)            
            elif car == 3:
                city=lines[lcv+3]
                c = Bus(name,tires,city)
                vehicles.append(c)

    totveh = 0
    cartot = 0
    tottires = 0
    
    totval = 0

    truckvalue = Truck("",0,0)

    cityname = ""

    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            totveh += 1
            tottires += vehicle.tires
            totval += vehicle.worth
            
            cartot+=vehicle.worth
        if isinstance(vehicle, Truck):
            totveh += 1
            tottires += vehicle.tires
            if (50000-(.25*truckvalue.miles)) > (50000-(.25*vehicle.miles)):
               truckvalue = vehicle
            totval += 50000-(.25*vehicle.miles)
        if isinstance(vehicle, Bus):
            totveh += 1
            tottires += vehicle.tires
            if len(vehicle.name) > len(cityname):
                cityname=vehicle.name
            totval += 50000

    print("Longest Home name for busses:",cityname)
    print("Lowest valued truck:",truckvalue.name)
    print("Total of tires:",tottires)


          

  except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
  main()

"""
Longest Home name for busses: MacBus

Lowest valued truck: Fred

Total of tires: 338
"""