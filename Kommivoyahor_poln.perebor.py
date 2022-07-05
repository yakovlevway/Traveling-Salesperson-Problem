####################################################
#####################################################
#####################################################Kommivoyahor polnii perebor
######################################################
import random
import numpy as np
def Marshrut(graph, s):
    puti = []
    for i in range(V):
        if i != s:
            puti.append(i)
    min_path = 100
    result_path = []
    
    while True:
        weight = 0
        path = []
        l = s
        for i in range(len(puti)):
            j = puti[i]
            weight += graph[l][j]
            path.append(str(l) + "->" + str(j))
            l = j
        path.append(str(j) + "->" + str(s))
        weight += graph[l][s]

        print("Маршрут:", path, "Его расстояние =", weight)
        if weight < min_path:
            result_path = path
            min_path = weight
        if not next1(puti):
            break
    return min_path, result_path

def next1(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1
        if i == -1:
            return False
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
    L[i], L[j] = L[j], L[i]
    left = i + 1
    right = n - 1
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return True
V = 5
s = 0
# A = [[0] * V for i in range(V)]

# for i in range(V):
#     for j in range(V):
#         A[i][j] = random.randint(1, 20)
# for i in range(V):
#     for j in range(V):
#         if i==j:
#             A[i][j]=0

A = np.random.randint(1, 20, size=(V, V))
for i in range(V):
    for j in range(V):
        if i==j:
            A[i,j]=0
W = np.maximum( A, A.transpose() )
print(W)
print('Min rasstoyanie i ego marshrut =',Marshrut(W,s))