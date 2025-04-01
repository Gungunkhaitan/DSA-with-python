def print_even(n):
    if n%2 ==0 and n>0:
        print_even(n-2)
        print(n,end=' ')
    elif n%2 !=0:
        n=n-1
        print_even(n)
print_even(9)