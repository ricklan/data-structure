def pow(num, exponent):
    if(exponent < 0):
        return 1/pow(num, -exponent)
    elif(exponent == 0):
        return 1
    else:
        if(exponent == 1):
            return num
    
        return num*pow(num, exponent-1)

print(pow(5, 3))
print(pow(10, 2))
print(pow(10, 0))
print(pow(5, -3))
print(pow(10, -2))
print(pow(10, 0))