class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)

        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in freq.items():
            buckets[count].append(num)
        print("\nBuckets (index = frequency):")
        for i in range(len(buckets)):
            if buckets[i]:
                print(f"Frequency {i}: {buckets[i]}")
        result = []
        for i in range (len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        