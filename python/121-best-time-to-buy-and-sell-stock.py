''' [Easy]

    Description
        You are given an array prices where prices[i] is the price of a given
        stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one
        stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction.
        If you cannot achieve any profit, return 0.

    Input
        prices = [7,1,5,3,6,4]
    Output
        5

    Hint
        maintain 2 variables, one for min price, one for max profix.
'''


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit


if __name__ == '__main__':
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    ans = sol.maxProfit(prices)
    print(ans)
