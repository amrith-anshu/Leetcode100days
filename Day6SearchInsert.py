class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num == target or num > target:
                return idx
        return len(nums)
