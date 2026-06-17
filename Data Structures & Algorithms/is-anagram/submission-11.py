class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_seen = list()
        t_seen = list()

        for i in range(len(s)):
            s_seen.append(s[i])
        for j in range(len(t)):
            t_seen.append(t[j])

        if s_seen == t_seen:
            return True




