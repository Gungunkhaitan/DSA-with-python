n = int(input("Enter n upto which you want to print fibonacci numbers: "))

first=0
second=1
print(first, end= ' ')
print(second, end= ' ')
for i in range(n-2):
    next=first+second
    print(next,end=' ')
    first=second
    second=next
print("\n")   