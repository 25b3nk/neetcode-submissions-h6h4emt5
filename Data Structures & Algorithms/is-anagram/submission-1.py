class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for c in list(s):
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1

        d2 = {}
        for c in list(t):
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1
        
        for k, v in d1.items():
            if k not in d2:
                return False
            if d2[k] != v:
                return False

        for k in d2.keys():
            if k not in d1:
                return False

        return True
