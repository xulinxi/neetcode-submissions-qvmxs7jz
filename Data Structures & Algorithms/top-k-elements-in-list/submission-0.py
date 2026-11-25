class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2
        Counter for nums + sort by count using priority queue to get top k frequent
        or
        Counter for nums + using dictionary methods

        or 
        Counter for nums + priority queue with size k

        python method notes:
        list methods: .sort() vs sorted

        dictionary sort, max... methods

        priority queue/heap
        """
        nums_counter = collections.Counter(nums)
        heap = []
        heapq.heapify(heap)


        for n, freq in nums_counter.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for freq, n in heap:
            # print(freq, n)
            res.append(n)

        return res














