class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for idx in range(len(strs[0])):
            char = strs[0][idx]

            for s in strs:
                if not (idx < len(s) and s[idx] == char ):
                    return prefix

            prefix += char
            
        return prefix