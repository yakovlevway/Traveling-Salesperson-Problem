import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# pip install beautifulsoup4
# pip install pymysql
# pip install nn
                                                            
import matplotlib.pyplot as plt
import numpy as np
from numpy import mgrid
n=10
a=np.zeros([n,n])
lenX, lenY = 10, 10


def printArr(arr):
    for i in range(lenX):
        for j in range(lenY):
            print("%.4f"%arr[i,j], end = ' ')
        print()
        
def rotate_matrix(mat):
    return np.rot90(mat)


array4=np.zeros([lenX,lenY])

for i in range(lenX):
    array4[lenX-1, i] = 1.0
    array4[i, lenX-1] = 1.0
array4[0, lenX-1] = 0.5
array4[lenX-1,0] = 0.5

for k in range(1000):
    for i in range(1,n-1):
        for j in range(1,n-1):
            array4[i,j] = 0.25*(array4[i+1,j]+array4[i-1,j]+array4[i,j+1]+array4[i,j-1])
            
print('Resultat: ')           
printArr(rotate_matrix(array4))
    
    
nx,ny = n-1, n-1
x,y=mgrid[0:1:((nx+1)*1j), 0:1:((ny+1)*1j)]
#plt.pcolor(y,x,a)
#plt.colorbar()
chisl=plt.contour(y,x,array4, 15, colors='black')
plt.clabel(chisl,fmt="%1.4f", inline=2, fontsize=15)
plt.title('Chislenii method', fontsize=17)
#plt.savefig('chisl')
plt.show(chisl)



