def subsets(nums):
    """
    Given an integer array nums of unique elements, return all possible subsets.
    The solution set must not contain duplicate subsets. Return the solution in any order.
    https://leetcode.com/problems/subsets/description/
    """
    res = []

    def backtrack(array, index):
        res.append(array[:])

        if len(array) == len(nums):
            return

        for i in range(index, len(nums)):
            array.append(nums[i])
            backtrack(array, i + 1)
            array.pop()

    backtrack([], 0)

    return res


nums = [1, 2, 3]
res = subsets(nums)
print(res)
