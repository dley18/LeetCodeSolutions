class MinStack {
    constructor() {
        this.stack = [];
        this.prefix_min_stack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (this.prefix_min_stack.length > 0) {
            let new_min = Math.min(this.prefix_min_stack[this.prefix_min_stack.length - 1], val);
            this.prefix_min_stack.push(new_min);
        } else {
            this.prefix_min_stack.push(val);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop();
        this.prefix_min_stack.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.prefix_min_stack[this.prefix_min_stack.length - 1];
    }
}