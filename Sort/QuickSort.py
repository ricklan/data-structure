def QuickSort(nums):
    n = len(nums)

    # Base Case
    if n <= 1:
        return nums

    # Choosing the first element as the pivot
    pivot = nums[0]

    # Partition the array into three parts:
    # 1. less: elements less than the pivot
    # 2. equal: elements equal to the pivot
    # 3. greater: elements greater than the pivot
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return QuickSort(less) + equal + QuickSort(greater)


if __name__ == "__main__":
    nums = [5, 2, 1, 6, 4]
    print(QuickSort(nums))
