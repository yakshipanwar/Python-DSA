"""
Problem: Container With Most Water
Category: Array / Two Pointers
Difficulty: Medium
Leetcode: https://leetcode.com/problems/container-with-most-water/

"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) *  (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else: 
                right -=1
        return max_area
        