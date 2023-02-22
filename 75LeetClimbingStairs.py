class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        i = 0
        f1, f2 = 1, 1
        while i <= n-2:
            f1, f2 = f2, f1+f2
            i += 1
        return f1
