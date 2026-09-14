class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        unique_s = set(s)
        for c in unique_s:
            if s.count(c) != t.count(c):
                return False
        return True