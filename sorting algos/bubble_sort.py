arr=[1,8,4,3,7,5,2,9,6]
n=len(arr)
for i in range(n-1):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)