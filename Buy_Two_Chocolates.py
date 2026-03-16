class Solution:
    def buyChoco(self, prices, money):
        first = float('inf')
        second = float('inf')
    
        for p in prices:
            if p < first:
                second = first
                first = p
            elif p < second:
                second = p
    
        total = first + second
    
        if total <= money:
            return money - total
        else:
            return money
        
#2nd approach
class Solution:
    def buyChoco(self, prices, money):
        prices.sort()
        total = prices[0] + prices[1]
        if total <= money:
            return money - total
        else:
            return money
        