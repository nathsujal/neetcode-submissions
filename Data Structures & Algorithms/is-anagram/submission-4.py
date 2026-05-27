class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for j in t:
            if j not in seen:
                # If any character present in `t` was not in `s` -> not an annagram
                return False

            seen[j] -= 1
        
        for v in seen.values():
            if v != 0:
                return False
        return True 