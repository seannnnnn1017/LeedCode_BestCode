class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0    
        seem={}
        max_len = 0
        for right in range(len(s)):
            print(seem, left, right, max_len)
            if s[right] in seem and seem[s[right]] >= left:
                left = seem[s[right]] + 1
            else:
                max_len = max(max_len, right - left + 1)
            seem[s[right]] = right
        return max_len

print(Solution().lengthOfLongestSubstring("abcabcdb")) # Output: 4
print(Solution().lengthOfLongestSubstring("bbbbb")) # Output: 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # Output: 3    
