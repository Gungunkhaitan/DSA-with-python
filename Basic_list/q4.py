n = int(input("Enter n upto which you want to print prime number: "))
def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
for i in range(2,n+1):
    if(isPrime(i)):
        print(i,end=' ')
print("\n")