def selectionSort(nums):
    n = len(nums)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    
    
    print(nums)

if(__name__ == "__main__"):
    array = [5, 2, 1, 6, 4]
    selectionSort(array)