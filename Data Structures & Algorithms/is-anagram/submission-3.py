class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = str()
        t_seen = str()
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    s_seen.append(s[i])
                    t_seen.append(t[j])
                else: 
                    return False