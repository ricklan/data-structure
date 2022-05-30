def fac(n):
    if(n <= 1):
        return 1
    return n*fac(n-1)

print(fac(5))
print(fac(0))
print(fac(10))
print(fac(8))