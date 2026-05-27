class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for j in t:
            if j in seen:
                seen[j] -= 1
            else:
                seen[j] = 1
        
        for k in seen.keys():
            if seen[k] != 0:
                return False
        return True 