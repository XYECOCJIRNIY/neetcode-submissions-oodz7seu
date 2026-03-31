class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for i in s:
            if i.isalnum():
                new += i
        return new.lower() == new.lower()[::-1]
        