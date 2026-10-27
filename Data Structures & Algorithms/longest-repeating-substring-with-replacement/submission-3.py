class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        max_fr = 0
        for right in range(len(s)):
            current_char = s[right]
            count[current_char]+=1
            max_fr = max(count[current_char], max_fr)

            win_size = right - left + 1
            re_required = win_size - max_fr
            if re_required>k:
                count[s[left]]-=1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len