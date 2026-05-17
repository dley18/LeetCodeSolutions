class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let indexes = Array.from(position.keys());
        indexes.sort((a, b) => position[b] - position[a]);

        let stack = [];

        for (let i = 0; i < indexes.length; i++) {
            const time = (target - position[indexes[i]]) / speed[indexes[i]]
            if (stack.length > 0 && time <= stack[stack.length - 1]) {
                continue;
            } else {
                stack.push(time);
            }
        }
        return stack.length;
    }
}
