class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {

        let prefixMax = new Array(height.length).fill(0)
        prefixMax[0] = height[0];
        for (let i = 1; i < height.length; i++) {
            prefixMax[i] = Math.max(prefixMax[i - 1], height[i]);
        }
        console.log("Prefix Max: ", prefixMax);
        let suffixMax = new Array(height.length).fill(0)
        suffixMax[height.length - 1] = height[height.length - 1]
        for (let i = height.length - 2; i >= 0; i--) {
            suffixMax[i] = Math.max(suffixMax[i + 1], height[i]);
        }
        console.log("Suffix Max: ", suffixMax);
        let total = 0;
        for (let i = 0; i < height.length; i++) {
            total += Math.min(prefixMax[i], suffixMax[i]) - height[i];
        }
        return total;
    }
}