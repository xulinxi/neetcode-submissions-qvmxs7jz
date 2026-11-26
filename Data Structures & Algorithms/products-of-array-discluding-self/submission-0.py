class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums    = [1,2,4,6]
                     i
        product = [1,1,1,1]   
                     i
        first iteration (from start): product[i] represent 1 preproduct (product of all elements before it), so start with i at 2nd num
        product[i] = product[i-1] *  nums[i-1]   
        product: 1,1,12,8
        second iteration from the end: left accR = 1
        product[i] = product[i] * accR; product[1] = product[1] * 24 = 24
        accR = accR * nums[i]; 6; 6 * 4 = 24

        TC: O(N)
        SC: (exclude result) O(1), with result O(N)

        python syntax notes:
        range(start, stop, step)
        """
        product = [1 for i in range(len(nums))]

        # from start
        for i in range(1, len(nums), 1):
            product[i] = product[i-1] * nums[i-1]   

        # from end
        accR = 1
        for j in range(len(nums)-1, -1, -1):
            product[j] = product[j] * accR
            accR = accR * nums[j]

        return product
