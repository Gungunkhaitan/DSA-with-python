def print_odd(i,n):
    if i%2 !=0 and i<=n:
        print_odd(i+2,n)
        print(i,end=' ')
    elif i%2 ==0:
        i=i+1
        print_odd(i,n)
print_odd(1,9)
print("\n")