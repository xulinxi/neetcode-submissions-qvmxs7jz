class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5] -> set: 2,3,4,5,10,20
         |

        curr_max, max_count = 1, 1

        for each num, check if it's first of its sequence (if num-1), if not skip
        - if first: while num + 1 in set: keep update curr_max, if not check curr_max vs max_count

        TC: O(N)
        SC: O(N)
        """
        # if len(nums) <2:
        #     return len(nums)
        nums_set = set(nums)
        # max_count = 1
        max_count = 0

        # for n in nums:
        for n in nums_set:

            # Only start from the beginning of a sequence
            if n-1 in nums_set:
                continue

            # Build the sequence once find the first in the sequence
            curr_count = 1
            curr = n
            while curr + 1 in nums_set:
                # n += 1
                curr_count += 1
                curr += 1

            # max_count = max(curr_count, max_count)
            max_count = max(max_count, curr-n+1)

        return max_count
