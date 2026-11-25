class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [3,4,5,6], target = 7
                

        Hash map + one-pass: check target - num in hashmap; if not found, store num->index

        TC: 1 iteration - O(N); N as num of numbers in nums    
        SC: used a dictionary to remember past num + its index
        return [past_index, curr_index]


        """
        diffMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffMap:
                return [diffMap[diff], i]

            diffMap[n] = i