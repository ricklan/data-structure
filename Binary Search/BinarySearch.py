def BinarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(BinarySearch(arr, 0))
    print(BinarySearch(arr, 1))
    print(BinarySearch(arr, 2))
    print(BinarySearch(arr, 3))
    print(BinarySearch(arr, 4))
    print(BinarySearch(arr, 5))
    print(BinarySearch(arr, 6))
