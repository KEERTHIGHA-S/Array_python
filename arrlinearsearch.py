a={10,20,30}
k=int(input("Enter the value for search in the array:"))
flag=0
for i in a:
    if(i==k):
        print("Elemtent found", i)
        flag=1
        break
if(flag==0):
    print("Element not found")