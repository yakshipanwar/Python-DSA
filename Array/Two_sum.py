"""
Problem: Two Sum
LeetCode Link: https://leetcode.com/problems/two-sum/
Approach: Hashmap for O(n) lookup
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash ={}
        for i, num in enumerate(nums):
            val = target - num
            if val in hash:
                return[hash[val], i]
            hash[num] = i