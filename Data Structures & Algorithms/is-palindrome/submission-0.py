class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        
        for ch in s:
            if ch.isalnum():
                filtered.append(ch.lower())

        s = "".join(filtered)

        stack = []
        for ch in range(len(s)//2):
            stack.append(s[ch])

        start = len(s)//2
        if len(s) % 2 != 0:
            start += 1

        for ch in range(start,len(s)):

            temp = stack.pop()

            if s[ch] != temp:
                return False

        return True
        