class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count = [0] * 26
        for ch in s1:
            s1_count[ord(ch)-ord('a')]+=1

        window = [0] * 26

        for i in range (len(s1)):
            window[ord(s2[i])-ord('a')]+=1

        for i in range(len(s1), len(s2)):
            if window == s1_count:
                return True
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            window[ord(s2[i]) - ord('a')] += 1

        # Final check for last window
        return window == s1_count

        

