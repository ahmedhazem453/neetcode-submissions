class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for idx in range(len(strs[0])):
            ans += strs[0][idx]

            for s in strs:
                if not (idx < len(s) and s[idx] == ans[-1]):
                    return ans[:-1]

        return ans