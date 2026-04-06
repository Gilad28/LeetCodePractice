class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dupli = set()
        biggest = 0

        for r in range(len(s)):
            while s[r] in dupli:
                dupli.remove(s[l])
                l += 1
            dupli.add(s[r])
            biggest = max(r - l + 1, biggest)
        
        return biggest
