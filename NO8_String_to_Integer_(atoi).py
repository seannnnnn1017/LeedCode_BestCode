
class Solution:
    def myAtoi(self, s: str):
        s = s.strip()  # 移除前導和尾隨空格
        if not s:
            return 0

        num = 0
        sign = 1
        index = 0

        # 判斷正負號
        if s[0] == '+' or s[0] == '-':
            sign = -1 if s[0] == '-' else 1
            index += 1

        # 轉換數字直到非數字字符
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        # 應用正負號
        num *= sign

        # 處理32位整數範圍
        num = max(-2**31, min(num, 2**31 - 1))

        return num

#print(Solution().myAtoi("12-43")) # Output: 42
print(Solution().myAtoi("s     -42")) # Output: -42