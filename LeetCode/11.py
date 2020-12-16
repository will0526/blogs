from typing import List


def maxArea(self, height: List[int]) -> int:
    start = 0
    end = len(height) - 1
    value = 0
    while start < end:
        width = end - start

        if height[start] < height[end]:
            high = height[start]
            start += 1
        else:
            high = height[end]
            end -= 1

        temp = high * width

        if temp > value:
            value = temp

    return value





