#int for whole
#float for decimals
#str for strings

car = input("Vehicle: ")
mile = 0
gal = 0
mpg = 0

if car == "1970 VW Bug":
    mile = 286
    gal = 9
if car == "1979 Firebird":
    mile = 412
    gal = 40
if car == "1980 Subaru":
    mile = 361
    gal = 18
if car == "1975 Cutlass":
    mile = 161
    gal = 11

mpg = float(mile)/gal
# since both numbers are ints, have to cast one or both as floats to get a decimal output

print (car," averaged ",round(mpg,10))

"""Vehicle: 1970 VW Bug
1970 VW Bug  averaged  31.7777777778"""