import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import rcParams
import math
import numpy as np
lenX, lenY = 10, 10
def analytical(x, y):
    u = 0.0
    u1=0.0
    n = 1
    eps = 0.001
    while n < 200:
        u1 = u
        u += 2 / math.sinh(math.pi * n) * (1 - math.cos(math.pi * n)) / (math.pi * n) * (math.sinh(math.pi * n * x) 
        * math.sin(math.pi * n * y) + math.sinh(math.pi * n * y) * math.sin(math.pi * n * x))
        if (abs(u - u1) < eps and u - u1 != 0):
            break
        n+=1
    return u

n = 10    

def printArr(arr):
    for i in range(lenX):
            print("%.4f"%arr[0,i], end = ' ')
    print()
    for i in range(lenX-2, 0, -1):
        for j in range(lenY):
            print("%.4f"%arr[i,j], end = ' ')
        print()    
    for i in range(lenX):
            print("%.4f"%arr[lenX-1,i], end = ' ')
            
            

a1=np.zeros([lenX,lenY])
array=np.zeros([lenX,lenY])

for i in range(n):
    a1[0, i] = 1.0
    a1[i, n-1] = 1.0
a1[0,0] = 0.5
a1[n-1, n-1] = 0.5

for i in range(1,lenX-1):
    for j in range(1,lenY-1):
        a1[i][j] = analytical(i / (lenX-1), j / (lenY-1))
       
printArr(a1)

for i in range(lenX):
    array[lenX-1, i] = 1.0
    array[i, lenX-1] = 1.0
array[0, lenX-1] = 0.5
array[lenX-1,0] = 0.5


for i in range(1,lenX-1):
    for j in range(1,lenY-1):
        array[i][j] = analytical(i / (lenX-1), j / (lenY-1))   



X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))
#plt.pcolor(Y,X,array)
#plt.colorbar()
i=plt.contour(Y,X,array,15, colors='black')
plt.clabel(i,fmt="%1.4f", inline=2, fontsize=15)
plt.title('Analiticheskii method', fontsize=17)
plt.show(i)