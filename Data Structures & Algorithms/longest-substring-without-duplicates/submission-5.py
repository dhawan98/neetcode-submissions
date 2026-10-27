class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        l = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[right])
            maxlen = max(maxlen, right-l+1)
        return maxlen