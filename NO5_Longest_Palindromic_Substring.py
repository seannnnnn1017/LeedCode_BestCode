class Solution: #Expand Around Center
    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s
        palindrome = ""
        for i in range(len(s)):
            
            # odd length palindrome
            p=0
            while i-p>=0 and i+p < len(s) and s[i-p] == s[i+p]:
                if 2*p+1 > len(palindrome):
                    palindrome = s[i-p:i+p+1]
                p+=1

            # even length palindrome
            l=i
            r=i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(palindrome):
        
                    palindrome = s[l:r+1]
                r+=1
                l-=1
        return palindrome
                
print(Solution().longestPalindrome("abb")) # "bab" or "aba"