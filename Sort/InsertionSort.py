def InsertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        num = nums[i]
        j = i-1
        while j >= 0 and num < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = num
    print(nums)


if(__name__ == "__main__"):
    array = [3, 1, 5, 3, 7, 2, -9]
    InsertionSort(array)