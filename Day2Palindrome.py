class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] 
    #checks the string using slicing from front and back
