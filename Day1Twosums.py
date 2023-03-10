class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        ''' enumerate adds counter to the list in the '''
        for i, j in enumerate(nums):
            r = target - j 
            if r in d: return [d[r], i] '''return the indices of the two numbers'''
            d[j] = i 
