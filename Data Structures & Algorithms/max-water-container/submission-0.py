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

        """
        max_area = float("-inf")

        l, r = 0, len(heights) - 1

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(curr_area, max_area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_area











