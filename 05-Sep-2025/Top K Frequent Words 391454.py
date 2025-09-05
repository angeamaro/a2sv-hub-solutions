# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        res = []

        n = len(words)
        buckets = [[] for _ in range(n + 1)]

        for word,freq in count.items():
            buckets[freq].append(word)

        for freq in range(n,0, -1):
            for word in sorted(buckets[freq]):
                res.append(word)
                if len(res) == k:
                    return res

        