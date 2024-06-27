import array as arr
k=arr.array('i',[])
for i in range(0,5):
    s=int(input("Enter the value"))
    k.append(s)
    print(k[i])
print("Reverse order")
for i in range(len(k)-1,-1,-1):
    print(k[i])
