class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while True:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
                
            if right <= left:
                return True

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False