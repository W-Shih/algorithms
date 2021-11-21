# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/57/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 20-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        results = []
        if numbers is None or len(numbers) < 3:
            return results

        numbers.sort()

        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self._two_sum_unique(numbers, i + 1, len(numbers) - 1, -numbers[i], results)

        return results

    def _two_sum_unique(self, nums, start_idx, end_idx, target, results):
        l, r = start_idx, end_idx
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == target:
                results.append([-target , nums[l], nums[r]])
                l, r = l + 1, r - 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif two_sum < target:
                l += 1
            else:
                r -= 1
