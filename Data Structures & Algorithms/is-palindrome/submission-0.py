class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join([char for char in s if char.isalnum()])
        string = string.lower()
        n = len(string)
        for i, char in enumerate(string):
            if char != string[n-i-1]:
                return False
        return True
