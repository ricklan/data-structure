def permutations(nums):
    """
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    https://leetcode.com/problems/permutations/description/
    """
    res = []

    def backtrack(array):
        if len(array) == len(nums):
            res.append(array[:])
            return

        for i in range(len(nums)):
            if nums[i] not in array:
                array.append(nums[i])
                backtrack(array)
                array.pop()

    backtrack([])

    return res


nums = [1, 2, 3]
res = permutations(nums)
print(res)
