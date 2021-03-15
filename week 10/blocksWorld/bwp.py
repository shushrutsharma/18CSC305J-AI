"""n = int(input("enter number of stacks"))
stac = []
for i in range(n):
        temp = input("enter stack 1").split()
        stac.append(temp)"""
        
stac = [['B','A'],['D'],['C']]
finalstac = ['B','C','A','D']
print("initial stack ",stac)
print("goal stack ",finalstac)
nu = 4
intermediate = []
def matrixIndex(st, arg):
        for i in range(len(st)):
                for j in range(len(st[i])):
                        if(st[i][j]==arg):
                                return(i,j)
for i in stac:
        for j in i:
                j = list(j)
                intermediate.append(j)
print("Step 1", intermediate)
for i in range (0,len(finalstac)):
        t = finalstac[i]
        if(i==0):
                flagm,flagn = matrixIndex(intermediate,t)
                continue
        else:
                intermediate[flagm].append(t)
                indm,indn = matrixIndex(intermediate,t)
                intermediate[indn][indm]=" "
                print("step "+str(i+1)+" ",intermediate)