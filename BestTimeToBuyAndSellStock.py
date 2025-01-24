class Solution(object):

    def __init__(self):
        self.stock_prices = {}

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        day = 1
        for price in prices:
            self.stock_prices[day] = price
            day += 1

        buy_price = 999999999
        buy_day = 0
        sell_price = 0
        sell_day = 0

        for day, price in self.stock_prices.items():
            if price < buy_price:
                buy_price = price
                buy_day = day
            
            if price > sell_price and day > buy_day:
                sell_price = price
                sell_day = day

        profit = sell_price - buy_price


        return "Buy Date: {0} \nSell Date: {1} \nProfit: {2}".format(buy_day, sell_day, profit)

sol = Solution()

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(sol.maxProfit(prices1))