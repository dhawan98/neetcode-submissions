class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i in strs:
            key = tuple(sorted(i))
            anagrams[key].append(i)
        return list(anagrams.values())