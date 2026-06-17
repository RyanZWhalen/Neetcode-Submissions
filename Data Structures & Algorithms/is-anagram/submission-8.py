class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_seen = set()
        t_seen = set()

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    s_seen.add(s[i])
                    t_seen.add(t[j])
                else: 
                    return False

        if s_seen == t_seen:
            return True




