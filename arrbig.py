a={1,25,34,4,655,60}
min=9999
max=-1
for i in a:
    if (min>i):
        min=i
    elif(max<i):
        max=i
    
print(min)
print(max)