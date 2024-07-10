
class Solution:
    def isPalindrome(self, x: int):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        left = str(x)[:len(str(x))//2]
        if len(str(x)) % 2 == 1:
            right = str(x)[len(str(x))//2+1:]
            

        elif len(str(x)) % 2 == 0:
            right = str(x)[len(str(x))//2:]

        return True if left == right[::-1] else False

class Solution:
    def isPalindrome(self, x: int):

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        # 當原始數字大於已翻轉的數字時，繼續執行循環
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # 如果是奇數位的數字，可以通過reversed_half//10去除中間的數字
        return x == reversed_half or x == reversed_half // 10

print(Solution().isPalindrome(1221)) # True
print(Solution().isPalindrome(12221)) # True