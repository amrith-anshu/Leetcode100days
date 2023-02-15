#find the duplicates in an list
#1st -> brute force
#2nd -> sorting
#3rd -> create hashset 
#optimal-- hashset and check length of set(nums) and nums.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        #we want to if the number is a duplicate
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
