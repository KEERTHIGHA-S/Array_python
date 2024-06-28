import array as arr
a=arr.array('i',[1,2,3,4,5])
i=0
while(i<len(a)):
    if(i>=2):
        print(a[i])
    i=i+1
j=0
while(j<len(a)):
    if(j<2):
        print(a[j])
    j=j+1