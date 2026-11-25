class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input: nums = [1,2,2,3,3,3], k = 2

        Output: [2,3]

        Counter:
        1: 1
        2: 2
        3: 3...

        - heap: ((freq, n)); heap > k: pop once
        left: top k; nlogk

        return [n for freq, n in heap]

        TC: O(nlogk)
        SC: O(N)

        """
        nums_counter = collections.Counter(nums)
        heap = []

        for n, freq in nums_counter.items(): # 1, 1
            heapq.heappush(heap, (freq, n)) # heap: (1, 1)

            if len(heap) > k: # (2, 2), (3, 3)
                heapq.heappop(heap)

        return [n for freq, n in heap] #[2, 3]




