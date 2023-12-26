pay = 4
hours = 1

"""
In ranges, the "stop" number is not included
Step is optional; 1 by default
If a start number isn't included, 'range(stop)' goes from 0 up to but not including stop
range(start, stop, step)
range(start, stop)
range(stop)
range(stop, step=num)
"""
#,"\t",

for hours in range(1,40+1,1):
    print(hours,"\t",pay*hours)