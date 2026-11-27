class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4] -> sort it [-4, -1, -1, 0, 1, 2]

        [-4, -1, -1, 0, 1, 2]
          i
             l
                           r
    
        res = []
        pre check for i: if not first num, check for dup (while i < len(nums) and i > 0 and nums[i] ==nums[i-1])
        3 pointers
        - check if meet the target sum (0)
            - if meet: add it to result; move one pointer (l) with dup check (while l < r and nums[l] == nums[l-1]: l += 1)
        - check until last 3 num

        TC: O(N^2) - N as nums count
        SC: O(1) (exclude res) - only use pointers; O(N) if includes results - worst case
        python syntax notes:
        array.sort() - no return
        sorted(iterable) - return sorted iterable
        """
        res = []
        n = len(nums)
        nums.sort()

        for i in range(0, n-2):
            # while 0 < i < n-3 and nums[i] == nums[i-1]:
            #     i += 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n-1

            while l < r:
               
                first, second, third = nums[i], nums[l], nums[r]
                # print(first, second, third)
                sum_ = first + second + third
                if sum_ == 0:
                    # res.append([i, l, r]) # 没有审题！ 应该加入num
                    res.append([first, second, third])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # print(first, second, third)

                # if sum_ > 0: # move r down; 这里要用elif!           
                elif sum_ > 0:
                    r -= 1
                else: # < 0; move l up
                    l += 1

        return res












