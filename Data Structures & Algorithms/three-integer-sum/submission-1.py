class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - remove dups
        - return outputs

        [-1,0,1,2,-1,-4] -> sort
        [-4, -1, -1, 0,1,2]
             i                   
                     l           
                       r
 l = i + 1
 r = at the end
 result = []
 check dup for i: for loop
    if i > 0, nums[i-1] == nums[i]: continue (skip)
 if total < 0: l += 1
    total > 0: r -= 1
    total == 0: 
        add it to results
        l -= 1; r+= 1

        check dup:
            while l < r, nums[l-1] == nums[l]: keep going
            while l < r, nums[r+1] == nums[r]: keep going

return results

TC: O(N^2)
SC: exclude results O(1) pointers; includes result (O(N^2))
        """

        result = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, length-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else: # == 0
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return result





















