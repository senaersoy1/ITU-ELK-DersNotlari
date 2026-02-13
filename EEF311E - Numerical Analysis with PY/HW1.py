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

line1 = "%dx0+%dx1=%d\n" % (i1, i2, r1)
line2 = "%dx0+%dx1=%d" % (i3, i4, r2)
Eqs = [line1, line2]

f = open("output.txt", "w+")
f.writelines(Eqs)
f.close()

#Gauss Elimination Method

a = np.array([[i1, i2], [i3, i4]],float)
b = np.array([r1, r2], float)
b = b[:,np.newaxis] 
n = len(b) 
x = np.zeros(n, float)
A_y = np.concatenate((a, b), axis = 1)
      
def printM(M):
    for i in range( M.shape[0]):
        for j in range( M.shape[1] ):
            return "%7.2f" %M[i,j]
                   
printM(a); 
        
for k in range(n-1): 
    for i in range(k+1, n): 
        fctr = a[k, k] / a[i, k]
        b[i] = fctr*b[i] - b[k]
        for j in range(k, n):
            a[i, j] = fctr*a[i, j] - a[k, j]
       
        printM(a); 
            
printM(a)
x[n-1] = b[n-1] / a[n-1, n-1] 

for i in range(n-2, -1, -1): 
    terms = 0
    for j in range(i+1, n):
        terms += a[i, j]*x[j]
    x[i] = (b[i] - terms)/a[i, i]

Output_Result_Gauss_Line1 = "The solution of the system by Gauss Elimination:\n"
Output_Result_Gauss_Line2 = "x0=%.4f\n" %x[0]
Output_Result_Gauss_Line3 = "x1=%.4f" %x[1]


#Jacobian Method

n = np.shape(b)[0]
t = np.full(n, -1.0, float) 
tnew = np.empty(n, float)
iterlimit = 100; tolerance = 1.0e-6

for iteration in range(iterlimit):
    for i in range(n): 
        s = 0
        for j in range(n): 
            if j != i:
                s += a[i, j]*x[j] 
        tnew[i] = (b[i]-s) / a[i,i]
    
    if (abs(tnew - t) < tolerance).all(): break
    else: t = np.copy(tnew)
    
Output_Result_Jacobi_Line1 = "The solution of the system by Jacobian Method:\n"
Output_Result_Jacobi_Line2 = "x0=%.4f\n" %t[0]
Output_Result_Jacobi_Line3 = "x1=%.4f\n\n" %t[1]


f_output_results = open("output_results.txt", "w+")
f_output_results.writelines([Output_Result_Jacobi_Line1, Output_Result_Jacobi_Line2, 
    Output_Result_Jacobi_Line3, Output_Result_Gauss_Line1, Output_Result_Gauss_Line2, Output_Result_Gauss_Line3])
f_output_results.close()



