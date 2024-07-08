class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0    
        if x < 0:
            x = -x
            x = int('-'+str(x)[::-1])
        else:
            x = int(str(x)[::-1])
        return x if -2**31 <= x <= 2**31-1 else 0
print(Solution().reverse(1534236469)) # Output: 321