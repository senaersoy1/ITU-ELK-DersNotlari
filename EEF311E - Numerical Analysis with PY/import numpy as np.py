import numpy as np
from numpy.linalg import matrix_rank

with open('input.txt', 'r') as file:
    lines = file.readlines()[1:]

data = [list(map(int, line.strip().split())) for line in lines]
np_array_data = np.array(data)
elements = np_array_data.reshape(1,6)

i1 = elements[0,0]
i2 = elements[0,1]
i3 = elements[0,2]
i4 = elements[0,3]
r1 = elements[0,4]
r2 = elements[0,5]

line1 = "%dx0 + %dx1 = %d\n" % (i1, i2, r1)
line2 = "%dx0 + %dx1 = %d" % (i3, i4, r2)
Eqs = [line1, line2]

print(np_array_data)