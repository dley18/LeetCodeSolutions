class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        let window = [];
        let max_arr = [];

        for (let r = 0; r < nums.length; r++) {
            while (window.length > 0 && nums[window[window.length - 1]] < nums[r]) {
                window.pop();
            }
            window.push(r);

            if (window[0] < r - k + 1) {
                window.shift();
            }

            if (r >= k - 1) {
                max_arr.push(nums[window[0]])
            }
        }
        return max_arr;
    }
}
