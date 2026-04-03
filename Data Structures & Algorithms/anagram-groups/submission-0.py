class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped = {}

        for word in strs:
            count = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            if key not in grouped:
                grouped[key] = []

            grouped[key].append(word)
        
        return list(grouped.values())
        