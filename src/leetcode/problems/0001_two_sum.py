"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers
 such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
 same element twice.

You can return the answer in any order.

---
url:
- https://leetcode.com/problems/two-sum
difficulty:
- easy
tags:
- array
- hash table
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_history = {}
        for idx, num in enumerate(nums):
            if target - num in nums_history:
                return [nums_history[target - num], idx]
            nums_history[num] = idx
