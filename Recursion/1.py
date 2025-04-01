def  print_natural(n):
    if n>0:
        print_natural(n-1)
        print(n, end=' ')

print_natural(5)