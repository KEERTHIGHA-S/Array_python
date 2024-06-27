i=[30,10,20]
s1=999999
s2=999999
for k in i:
    if(k<s1):
        s2=s1
        s1=k
    elif(k<s2):
        s2=k
print(s1)
print(s2)