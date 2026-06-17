class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = set()
        t_seen = set()
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    s_seen.append(s[i])
                    t_seen.append(t[j])
                else: 
                    return False