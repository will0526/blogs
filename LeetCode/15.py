# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# 思路：1，先排序。2，遍历
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        result = list()

        for first in range(n):
            if first>0 and nums[first ] == nums[first -1]:
                continue

            target = -nums[first]
            third = n -1
            for second in range(first +1, n):
                if second>first+1 and nums[second] == nums[second -1]:
                    continue
                while second< third and nums[second]+nums[third]>target:
                    third -= 1

                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    result.append([nums[first],nums[second],nums[third]])

        return result
