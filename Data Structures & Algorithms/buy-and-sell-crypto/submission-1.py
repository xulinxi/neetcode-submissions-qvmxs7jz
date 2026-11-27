class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [10,1,5,6,7,1]
            |
                   

        keep prev min
        keep max_profit

        
        if curr price < min: update min

        (if curr > min)for every day: profit = curr price - min price
        max_profit = max(max_profit, curr prodit)



        return max_profit

        TC: O(N)
        SC: O(1)

        """
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
                continue # no need to check profit

            profit = price - min_price
            max_profit = max(max_profit, profit)


        return max_profit

            


