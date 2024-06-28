'''import array as arr
a=arr.array('i',[1,2,3])
b=arr.array('i',[1,2,3])
c=arr.array('i',[])
for i in range(0,len(a)):
    c[i]=a[i]+b[i]
    print(c[i])'''
    
a=[1,1,8,1,1,4,3]
b=[1,1,2,1,1,7]
c=[]


len1=len(a)
len2=len(b)
length=len1 if len1>len2 else len2
#print(length)
addlen=len1 if len1<len2 else len2
#print(addlen)

for i in range(0,addlen):
    c=a[i]+b[i]
    print(c)
print("Remaining elements after adding")
i=i+1
while(i<length):
    if(len1<len2):
        print(b[i])
    else:
        print(a[i])
    i=i+1