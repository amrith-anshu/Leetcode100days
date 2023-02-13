class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        #search acrossing the list
        for j in nums:
            if j not in nums[:i]:
                nums[i]=j
                i+=1
        return i
