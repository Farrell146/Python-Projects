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

"""
1        4
2        8
3        12
4        16
5        20
6        24
7        28
8        32
9        36
10       40
11       44
12       48
13       52
14       56
15       60
16       64
17       68
18       72
19       76
20       80
21       84
22       88
23       92
24       96
25       100
26       104
27       108
28       112
29       116
30       120
31       124
32       128
33       132
34       136
35       140
36       144
37       148
38       152
39       156
40       160
"""