class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,4,6]

            res = [1, 1, 2, 8] 
                            i


            prefix: iterate from start; [1, 1, 2, 8]
            res[i] = res[i-1] * nums[i-1]
            res[1] = res[0] * nums[0] = 1
            res[2] = res[1] * nums[1] = 1 * 2 = 2

            suffix: iterate from end; [48,24,12,8]
            [1, 1, 2, 8]
                    i
            right = 8
            res[i] = res[i] * right = 
            right = right * nums[i] = 1 * 6 = 6
            res[3] = res[3] * right = 8 * 1 = 8
            right = right * nums[i] = 1 * 6 = 6
            res[2] = res[2] * right = 2 * 6 = 12
            ...
            TC: O(N)
            SC: (exlcude res) O(1); (include res) O(N)


        Output: [48,24,12,8]


        """
        n = len(nums)
        res = [1] * n

        # suffix iteration from the start
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        # prefix iteration from the end
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res















