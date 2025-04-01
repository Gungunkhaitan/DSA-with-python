def sum_odd(n):
    if n<=0:
        return 0
    else:
        if n%2==0:
            return sum_odd(n-1)
        else:
            return n+sum_odd(n-2)

print(sum_odd(5))
print(sum_odd(6))