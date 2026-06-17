class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_seen = sorted(s)   # sorted() turns the string into a sorted list of chars
        t_seen = sorted(t)

        return s_seen == t_seen




