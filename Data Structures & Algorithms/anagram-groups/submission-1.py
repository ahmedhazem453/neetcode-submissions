class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}

        for s in strs:
            sortedS = ''.join(sorted(s))

            if sortedS in dct:
                dct[sortedS].append(s)
            else:
                dct[sortedS] = [s]

        return list(dct.values())