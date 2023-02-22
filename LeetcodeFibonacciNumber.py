class Solution:
    def fib(self, n: int) -> int:
        prev1 = 0
        prev2 = 1

        if n <= 1:
            return n

        for i in range(2,n+1):
            ans = prev1 + prev2
            prev1 = prev2
            prev2 = ans
        
        return ans
      #the current values is sum of the last two previous values and update the previous values.
