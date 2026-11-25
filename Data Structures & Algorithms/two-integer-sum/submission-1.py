class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [3,4,5,6], target = 7
                  |
                0 1 
                [0,1]

        HashMap visited  (num, index) + one Pass
        check if diff (target - curr num) in visited
        HashMap:
        3: 0

        [diff_index, curr_index]
        TC: O(N)
        SC: O(N)
        """
        diffMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[n] = i