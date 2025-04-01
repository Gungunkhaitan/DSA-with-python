def print_odd(n):
    if n%2 !=0 and n>0:
        print_odd(n-2)
        print(n,end=' ')
    elif n%2==0:
        n=n-1
        print_odd(n)
print_odd(9)