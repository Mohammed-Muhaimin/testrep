L1=[]
num = int(input('enter the values'))
for i in range(num):
    val=int(input('enter the elements'))
    L1.append(val)
print (L1)

mean=sum(L1)/len(L1)
print('mean is=',mean)

total=0
for i in L1:
    total+=(val-mean)**2
    var=total/num

print('variance is ',var)