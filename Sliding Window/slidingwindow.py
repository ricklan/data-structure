def findAllSubarries(array, target):
    '''
    This function finds all subarries that add up to a sum
    '''

    res = []
    left = 0
    right = 0
    new_sum = 0

    while right < len(array):
        new_sum = sum(array[left:right + 1])
        if(new_sum == target):
            res.append(array[left:right + 1])
            right += 1
        elif (new_sum < target):
            right += 1
        else:
            left += 1
    
    
    return res

def longestSubstringWithoutRepeatingChars(string):
    '''
    This function finds the longest substring without repeating characters
    '''

    longestSubstr = ""
    left = 0
    right = 0
    seenChars = {}
    substr = ""

    while (right < len(string)):
        newChar = string[right]
        if(newChar not in seenChars):
            seenChars[newChar] = 1
            substr += newChar
            right += 1
            if(len(substr) > len(longestSubstr)):
                longestSubstr = substr
        else:
            firstChar = substr[0]
            substr = substr[1:]
            seenChars.pop(firstChar)
            left += 1
        

    return longestSubstr

if(__name__ == "__main__"):
    arr = [1,3,2,4,5]
    target = 6
    print(findAllSubarries(arr, target))

    arr2 = [6]
    target2 = 6
    print(findAllSubarries(arr2, target2))

    str1 = "abcbbcab"
    print(longestSubstringWithoutRepeatingChars(str1))