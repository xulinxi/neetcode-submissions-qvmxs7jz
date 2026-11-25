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
        .sort(): list method, modified in place, return None, use on list only, slightly faster, no memory needed
        sorted: Build-in function, unchange, return sorted list or other iterable, use on any iterable (lists, tuples, strings, dicts, sets), slightly slower, uses extra memory to copy data

        dictionary sort, max... methods
        sort:
d = {1: 1, 2: 2, 3: 3}

# Sort by value, descending
sorted(d.items(), key=lambda x: x[1], reverse=True)

# Get key with maximum value
max(d, key=d.get)

# Get key-value pair with maximum value
max(d.items(), key=lambda x: x[1])

        max:
        top k:

        Counter:
        .most_common(k)
        counts = Counter(["a", "b", "a", "c", "a", "b"])
        print(counts.most_common(2))  # [('a', 3), ('b', 2)]

        priority queue/heap

Method	               用途	                 Complexity
heapq.heapify(heap)	Convert list into heap	O(n)
heapq.heappush(heap, x)	Insert element	O(log n)
heapq.heappop(heap)	Remove smallest	O(log n)
heapq.nlargest(k, iterable)	Get largest k	O(n log k)
heapq.nsmallest(k, iterable)	Get smallest k	O(n log k)

        heapify 什么时候是有必要的？


Counter(nums)
counter.items()

heapq.heappush(heap, (freq, num))
heapq.heappop(heap)

sorted(d.items(), key=lambda x: x[1])
max(d, key=d.get)

[num for freq, num in heap]



假设：
- n = total number of elements
- u = number of unique elements
- k = number of elements to return
Approach	Time Complexity	Space
Counter + Sorting	O(n + u log u)	O(u)
Counter + Min Heap	O(n + u log k)	O(u + k)
Counter.most_common(k)	O(n + u log k)	O(u + k)
Counter + Bucket Sort	O(n)	O(n)

Python 内部优化
most_common() 会根据参数选择不同的方法：
Syntax	          Algorithm	Time（不含 Counter）
most_common()	Sorting	O(u log u)
most_common(1)	max()	O(u)
most_common(k)，k 小于 u	Heap	O(u log k)，k ≥ 2
most_common(k)，k ≥ u	Sorting	O(u log u)
        """
        nums_counter = collections.Counter(nums)
        heap = []
        # heapq.heapify(heap)


        for n, freq in nums_counter.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)

        # res = []
        # for freq, n in heap:
        #     # print(freq, n)
        #     res.append(n)

        # return res
        return [n for freq, n in heap]














