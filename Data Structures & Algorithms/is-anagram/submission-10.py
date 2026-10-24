class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for char in s:
            count1[char] = count1.get(char, 0) + 1
        for charT in t:
            count2[charT] = count2.get(charT, 0) + 1
        print(count1)
        print(count2)
        return (count1 == count2)