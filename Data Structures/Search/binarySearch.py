def binarySearch(array, value):
    left = 0
    right = len(array) - 1
    
    while(left <= right):
        mid = (left + right) // 2
        if(value == array[mid]):
            return mid
        elif(value < array[mid]):
            right = mid - 1
        else:
            left = mid + 1
    
    return None

def binarySearchRecursive(array, value, left, right):
    if(left <= right):
        mid = (left + right) // 2
        if(array[mid] == value):
            return mid
        elif(value < array[mid]):
            return binarySearchRecursive(array, value, left, mid - 1)
        else:
            return binarySearchRecursive(array, value, mid + 1, right)
    else:
        return None

if(__name__ == "__main__"):
    arr = [1,2,3,4,5]
    print("Iterative Search")
    print(binarySearch(arr, 0))
    print(binarySearch(arr, 1))
    print(binarySearch(arr, 2))
    print(binarySearch(arr, 3))
    print(binarySearch(arr, 4))
    print(binarySearch(arr, 5))
    print(binarySearch(arr, 6))
    print("Recursive Search")
    print(binarySearchRecursive(arr, 0, 0, 4))
    print(binarySearchRecursive(arr, 1, 0, 4))
    print(binarySearchRecursive(arr, 2, 0, 4))
    print(binarySearchRecursive(arr, 3, 0, 4))
    print(binarySearchRecursive(arr, 4, 0, 4))
    print(binarySearchRecursive(arr, 5, 0, 4))
    print(binarySearchRecursive(arr, 6, 0, 4))
