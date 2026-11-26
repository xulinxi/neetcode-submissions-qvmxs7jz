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
        
        [1] * n 什么时候不能用？
        * n 是重复引用（shallow repetition），不是每次都创建一个全新的 object。
        Immutable objects（可以安全使用）
        Mutable objects（需要小心）。因为三个位置实际上指向同一个 list object。
        场景	推荐
      不需要使用 loop variable	_
      普通 loop	i, j, k
      Prefix / Suffix	left, right
      累积乘积	prefix, suffix
      初始化 immutable values	[value] * n
      初始化 mutable objects	[factory() for _ in range(n)]

        """

        n = len(nums)
        # product = [1 for i in range(len(nums))]
        res = [1] * n

        # from start
        # Pass 1: Calculate prefix products
        # for i in range(1, len(nums), 1):
        for i in range(1, n):
            # product[i] = product[i-1] * nums[i-1]   
            res[i] = res[i-1] * nums[i-1]

        # from end
        # Pass 2: Multiply by suffix products
        # accR = 1
        right = 1
        # for j in range(len(nums)-1, -1, -1):
        for i in range(n-1, -1, -1):
            # product[j] = product[j] * accR
            res[i] *= right
            # accR = accR * nums[j]
            right *= nums[i]

        # return product
        return res
