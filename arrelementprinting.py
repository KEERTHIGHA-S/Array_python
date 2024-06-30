i=[1,2,5,8,10,11]
j=len(i)
print(j)
k=0
while(k<j-1):
    n1=i[k]
    n2=i[k+1]
    small=n1 if n1<n2 else n2
    big=n1 if n1>n2 else n2
    for num in range(small+1,big):
        print(num)
    k=k+1
    