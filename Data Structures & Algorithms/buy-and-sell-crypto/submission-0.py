class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        keep previous min and update max_profit if curr profit is greater
        [10,1,5,6,7,1]
         |

         max_profit = 0
         if curr price < min:
            update and recalculate profit

        return max_profit 
        """
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            
            if price < min_price:
                min_price = price
                continue
            
            profit = price - min_price
            max_profit = max(max_profit, profit)

            
        return max_profit