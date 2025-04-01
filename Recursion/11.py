def sum_of_squares(n):
    
    if n==0:
        return 0
    else:
        return (n*n)+sum_of_squares(n-1)
    
print(sum_of_squares(3))
print(sum_of_squares(2))
