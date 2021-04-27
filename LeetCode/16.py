# 寻找三数之和最接近的解
# 思路：1，先排序。2,双指针定位second 和 third
from typing import List


class Solution:
    def threeSum(self, nums: List[int], target) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        result = 10 ** 5

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = n - 1
            while second < third:

                res = nums[first] + nums[second] + nums[third]
                if res == target:
                    return target

                if abs(result - target) > abs(res - target):
                    result = res

                if res < target:

                    second0 = second + 1
                    # 去重
                    while second0 < third and nums[second0] == nums[second]:
                        second0 += 1
                    second = second0

                if res > target:
                    third0 = third - 1
                    while third0 > second and nums[third0] == nums[third]:
                        third0 -= 1

                    third = third0
        return result
