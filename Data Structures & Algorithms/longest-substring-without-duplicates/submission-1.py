class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in char_map:
                l = max(l, char_map[s[r]] + 1)

            char_map[s[r]] = r
            res = max((r - l) + 1,res)

        return res