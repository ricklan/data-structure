def palindrome(string):
    if(len(string) <= 1):
        return True
    
    return palindrome(string[1:-1]) and string[0] == string[-1]


print(palindrome("racecar"))
print(palindrome("car"))
print(palindrome("civic"))