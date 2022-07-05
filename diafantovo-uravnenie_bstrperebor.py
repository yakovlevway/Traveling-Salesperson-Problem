#####################################################
#####################################################Diofantovo uravneniye polnii perebor
#####################################################
######################################################
k=0
for a in range (31):
    for b in range(16):
        for c in range(11):
            for d in range(8):
                if (a + 2 * b + 3 * c + 4 * d == 30):
                    k+=1
                    print("a=", a, end = ", ")
                    print("b=", b, end = ", ")
                    print("c=",c, end = ", ")
                    print("d=",d, end = '\n')
print('kolichestvo naidenih rehenii:', k)