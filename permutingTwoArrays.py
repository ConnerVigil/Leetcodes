class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        values = {}  # Initialize dictionary to store {value, index} pairs
        for i, value in enumerate(nums):  # Loop through nums
            complement = target - value

            if complement in values:  # Check if we have already passed the other value needed to make target
                return [values[complement], i]  # Return indexes of both values
            else:
                values[value] = i  # Put {value, i} pair in dictionary


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
