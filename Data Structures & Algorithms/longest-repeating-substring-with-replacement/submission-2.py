class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_len=0
        left=0
        max_freq=0

        for right in range(len(s)):
            current_char = s[right]
            count[current_char]+=1
            max_freq = max(max_freq, count[current_char])

            window_size = right-left+1
            replacements = window_size-max_freq
            if replacements>k:
                count[s[left]]-=1
                left+=1
            
            max_len = max(max_len, right-left+1)

        return max_len