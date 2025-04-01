def print_even(i,n):
    if i%2 ==0 and i<=n:
        print_even(i+2,n)
        print(i,end=' ')
    elif i%2 !=0:
        i=i+1
        print_even(i,n)
print_even(1,9)