def BubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)

if(__name__ == "__main__"):
    array1 = [5, 2, 1, 6, 2]
    BubbleSort(array1) 

    array2 = [5,1,2,4,8]
    BubbleSort(array2)