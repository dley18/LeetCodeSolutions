class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let minBuy = prices[0];
        let profit = 0;

        for (let i = 1; i < prices.length; i++) {
            let newProfit = prices[i] - minBuy;
            profit = Math.max(profit, newProfit);
            minBuy = Math.min(minBuy, prices[i]);
        }
        
        return profit;
    }
}
 