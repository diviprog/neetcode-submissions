class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = [char.lower() for char in s if char.isalnum()]
        backward = forward[::-1]
        return forward == backward