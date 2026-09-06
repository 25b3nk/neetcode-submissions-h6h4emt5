class Solution:
    def sortChars(self, s: str) -> str:
        l = list(s)
        l.sort()
        return "".join(l)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sortedS = self.sortChars(s)
            if sortedS in d:
                d[sortedS].append(s)
            else:
                d[sortedS] = [s]

        output = []
        for s in d:
            output.append(d[s])
        return output
        
