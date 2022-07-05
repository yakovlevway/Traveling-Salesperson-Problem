import numpy as np
import matplotlib.pyplot as plt
def printArr(arr):
    for i in range(lenX):
        for j in range(lenY):
            print("%.4f"%arr[i,j], end = ' ')
        print()
        
lenX, lenY = 10, 10

a1=np.zeros([lenX,lenY])

for i in range(n):
    a1[0, i] = 1.0
    a1[i, n-1] = 1.0
a1[0,0] = 0.5
a1[n-1, n-1] = 0.5

t = 0.001
temp1 = a1.copy()
h = 1 / (lenX+5)
for k in range(100):
    for i in range(1, lenX - 1):
        for j in range(1, lenY - 1):
            temp1[i][j] = a1[i][j]
            a1[i][j] = temp1[i][j] + t/(h*h) * (a1[i+1][j] + a1[i-1][j] + a1[i][j+1] + a1[i][j-1] - 4*a1[i][j])
printArr(a1)

array2=np.zeros([lenX,lenY])
for i in range(lenX):
    array2[lenX-1, i] = 1.0
    array2[i, lenX-1] = 1.0
array2[0, lenX-1] = 0.5
array2[lenX-1,0] = 0.5


t = 0.001
temp1 = array2.copy()

for k in range(100):
    for i in range(1, lenX - 1):
        for j in range(1, lenY - 1):
            temp1[i][j] = array2[i][j]
            array2[i][j] = temp1[i][j] + t/(h*h) * (array2[i+1][j] + array2[i-1][j] + array2[i][j+1] + array2[i][j-1] - 4*array2[i][j])


X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))
#plt.pcolor(Y,X,array)
#plt.colorbar()
i=plt.contour(Y,X,array2,15, colors='black')
plt.clabel(i,fmt="%1.4f", inline=2, fontsize=15)
plt.title('Evolutionii method', fontsize=17)
plt.show(i)