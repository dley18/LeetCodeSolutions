class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let profit = 0;

        for (let i = 0; i < prices.length; i++) {
            const buyValues = prices.slice(0, i);
            const minBuy = Math.min(...buyValues);
            profit = Math.max(profit, prices[i] - minBuy);
        }
        
        return profit;
    }
}
 