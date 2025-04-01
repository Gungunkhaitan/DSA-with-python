def quicksort(arr,left,right):
    if left<right:
        pivot_pos=partition(arr,left,right)
        quicksort(arr,left,pivot_pos-1)
        quicksort(arr,pivot_pos+1,right)

def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while arr[i]<pivot and i <right:
            i+=1
        while arr[j]>pivot and j>left:
            j-=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i

arr=[22,11,88,66,55,77,33,44]
quicksort(arr,0,len(arr)-1)
print(arr)