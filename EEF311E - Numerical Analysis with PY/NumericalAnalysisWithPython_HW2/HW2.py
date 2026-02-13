import numpy as np
import sys

with open('input.txt', 'r') as file:
    lines = file.readlines()

line1 = lines[0]
line2 = lines[1]

values1 = line1.split('=')[1].split(',')
values2 = line2.split('=')[1].split(',')

int_values1 = [int(value) for value in values1]
int_values2 = [int(value) for value in values2]

a1 = int_values1[0]
b1 = int_values1[1]
c1 = int_values1[2]

a2 = int_values2[0]
b2 = int_values2[1]
c2 = int_values2[2]

peak1 = -b1/(2*a1)
peak2 = -b2/(2*a2)

iteration = 100
tolerance = 1e-6

def y1(x):
    return a1*x**2 + b1*x + c1

def y2(x):
    return a2*x**2 + b2*x + c2

def find_interval_y1(k):
    k2 = k+0.1
    value1 = y1(k)
    value2 = y1(k2)
    while value1 * value2 > 0:
        k = k2
        k2 = k+0.1
        value1 = y1(k)
        value2 = y1(k2)
    else:
        interval1 = k
        interval2 = k2
    intervals = [interval1, interval2]
    return intervals

def find_negative_interval_y1(k):
    k2 = k-0.1
    value1 = y1(k)
    value2 = y1(k2)
    while value1 * value2 > 0:
        k = k2
        k2 = k-0.1
        value1 = y1(k)
        value2 = y1(k2)
    else:
        interval1 = k
        interval2 = k2
    intervals = [interval1, interval2]
    return intervals

def find_interval_y2(k):
    k2 = k+0.1
    value1 = y2(k)
    value2 = y2(k2)
    while value1 * value2 > 0:
        k = k2
        k2 = k+0.1
        value1 = y2(k)
        value2 = y2(k2)
    else:
        interval1 = k
        interval2 = k2
    intervals = [interval1, interval2]
    return intervals

def find_negative_interval_y2(k):
    k2 = k-0.1
    value1 = y2(k)
    value2 = y2(k2)
    while value1 * value2 > 0:
        k = k2
        k2 = k-0.1
        value1 = y2(k)
        value2 = y2(k2)
    else:
        interval1 = k
        interval2 = k2
    intervals = [interval1, interval2]
    return intervals
    

i1y1 = find_interval_y1(peak1)[0]
i2y1 = find_interval_y1(peak1)[1]
i3y1 = find_negative_interval_y1(peak1)[0]
i4y1 = find_negative_interval_y1(peak1)[1]

i1y2 = find_interval_y2(peak2)[0]
i2y2 = find_interval_y2(peak2)[1]
i3y2 = find_negative_interval_y2(peak1)[0]
i4y2 = find_negative_interval_y2(peak1)[1]

I1 = i1y1;I2 = i2y1;I3 = i3y1;I4 = i4y1;I5 = i1y2;I6 = i2y2;I7 = i3y2;I8 = i4y2

for i1 in range(1, iteration):
    xh1 = (i1y1 + i2y1)/2

    if abs(y1(xh1)) < tolerance:
        root1 = xh1
        break
    elif y1(i1y1) * y1(xh1) < 0:
        i2y1 = xh1
    else:
        i1y1 = xh1

for i2 in range(1, iteration):
    xh2 = (i3y1 + i4y1)/2

    if abs(y1(xh2)) < tolerance:
        root2 = xh2
        break
    elif y1(i3y1) * y1(xh2) < 0:
        i4y1 = xh2
    else:
        i3y1 = xh2

for i3 in range(1, iteration):
    xh3 = (i1y2 + i2y2)/2

    if abs(y2(xh3)) < tolerance:
        root3 = xh3
        break
    elif y2(i1y2) * y2(xh3) < 0:
        i2y2 = xh3
    else:
        i1y2 = xh3

for i4 in range(1, iteration):
    xh4 = (i3y2 + i4y2)/2

    if abs(y2(xh4)) < tolerance:
        root4 = xh4
        break
    elif y2(i3y2) * y2(xh4) < 0:
        i4y2 = xh4
    else:
        i3y2 = xh4

Passage1 = "Given equations: \ny1= %dx**2%dx+%d\ny1= %dx**2%dx+%d\n" %(a1, b1, c1, a2, b2, c2)
Passage2 = "The roots of y1:\nInterval: %.2f-%.2f\nIteration: %d\nx1=%d\nInterval: %.2f-%.2f\nIteration: %d\nx2=%d\n" %(I1, I2, i1, root1, I3, I4, i2, root2)
Passage3 = "The roots of y2:\nInterval: %.2f-%.2f\nIteration: %d\nx1=%d\nInterval: %.2f-%.2f\nIteration: %d\nx2=%d" %(I5, I6, i3, root3, I7, I8, i4, root4)

f_output_results = open("output.txt", "w+")
f_output_results.writelines([Passage1,Passage2,Passage3])
f_output_results.close()
