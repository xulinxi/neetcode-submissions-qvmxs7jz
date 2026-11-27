class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        max_area = float("-inf")

        [1,7,2,5,4,7,3,6]
         l
                       r

        We use 2 pointers to find max l and r height while calculating the area, replace max_area if curr_area is larger
        area = min(heights[l], heights[r]) * (r - l)

        r -= 1 if heights[r] < heights[l]
        else:
            l += 1

        TC: one iteration: O(N)
        SC: two pointers: O(1)
        """
        
        max_area = 0


        left, right = 0, len(heights) - 1

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            width = right - left
            area = min(left_height, right_height) * width
            max_area = max(max_area, area)

            if left_height <= right_height:
                left += 1
            else:
                right -= 1
        return max_area











