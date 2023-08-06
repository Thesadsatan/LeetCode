class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sample = strs[0]
        pr = ''

        for i in range(len(sample)):

            for pref in strs:

                if  i == len(pref) or pref[i] != sample[i]:
                    return pr

            pr = pr + pref[i]         

        return pr