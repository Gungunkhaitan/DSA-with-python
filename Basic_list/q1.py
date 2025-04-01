from array import *
arr=array('i',[2,5,4,3,1,6])
print("\nBefore sorting: ")
for i in range(6):
    print(arr[i],end=' ')
print("\n\nAfter sorting: ")
for i in range(5):
    for j in range(5):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
for i in range(6):
    print(arr[i],end=' ')
print("\n")