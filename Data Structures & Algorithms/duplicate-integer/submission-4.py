class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        - sort + one time iteration: TC: O(nlogn); SC: O(1)
        - set: check length: different length: then true; TC: O(n); SC: O(n) - n as num of items in the nums; another way using set: iterate while putting item in the set, could optimize for nums like: 1, 1, 1,....

        pick 2nd set method
        """

        unique_set = set()
        for n in nums:
            if n in unique_set:
                return True
            unique_set.add(n)
        return False
