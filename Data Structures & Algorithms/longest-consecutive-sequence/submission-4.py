class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums = [2,20,4,10,3,4,5] -> set
        max_count = 1
                          
        * check from the first num in its sequence: check if n - 1: exist: not first num in the sequence: skip

        set: 2, 20, 4, 10, 3, 5
             |

            curr + 1; 3
            curr_count += 1...


    end of this sequence: check max_count vs curr count


    return max_count

    TC: O(N)
    SC: O(N)
        """
        nums_set = set(nums)
        max_count = 0

        for n in nums_set:
            if n-1 in nums_set: # not first num in the sequence: skip
                continue

            # first
            curr = n
            curr_count = 1
            while curr + 1 in nums_set:
                curr += 1
                curr_count += 1

            max_count = max(max_count, curr_count)
        return max_count












