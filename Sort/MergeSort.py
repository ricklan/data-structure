def MergeSort(nums):
    n = len(nums)

    if n <= 1:
        return nums

    mid = n // 2
    left = MergeSort(nums[:mid])
    right = MergeSort(nums[mid:])

    return Merge(left, right)


def Merge(left_subarray, right_subarray):
    sorted_array = []
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(left_subarray) and right_pointer < len(right_subarray):
        left_num = left_subarray[left_pointer]
        right_num = right_subarray[right_pointer]

        if left_num < right_num:
            sorted_array.append(left_num)
            left_pointer += 1
        elif right_num < left_num:
            sorted_array.append(right_num)
            right_pointer += 1
        else:
            sorted_array.append(left_num)
            sorted_array.append(right_num)
            left_pointer += 1
            right_pointer += 1

    sorted_array += left_subarray[left_pointer:]
    sorted_array += right_subarray[right_pointer:]

    return sorted_array


if __name__ == "__main__":
    nums = [5, 2, 1, 6, 4]
    print(MergeSort(nums))
