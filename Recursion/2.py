def  print_natural(i,n):
    if i<=n:
        print_natural(i+1,n)
        print(i, end=' ')

print_natural(1,5)