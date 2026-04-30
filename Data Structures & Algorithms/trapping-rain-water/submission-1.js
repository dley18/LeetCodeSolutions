class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let prefixMax = new Array(height.length).fill(0);
        prefixMax[0] = height[0];
        let suffixMax = new Array(height.length).fill(0);
        suffixMax[height.length - 1] = height[height.length - 1];
        let total = 0;
        let left = 1;
        let right = height.length - 2;
        
        while (left < height.length && right >= 0) {
            prefixMax[left] = Math.max(prefixMax[left - 1], height[left]);
            left += 1;
            suffixMax[right] = Math.max(suffixMax[right + 1], height[right]);
            right -= 1;
        }

        for (let i = 0; i < height.length; i++) {
            total += Math.min(suffixMax[i], prefixMax[i]) - height[i];
        }
        return total;
    }
}