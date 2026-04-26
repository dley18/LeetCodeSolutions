impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut table = HashSet::new();
        for num in nums {
            if table.contains(&num) {
                return true;
            }
            table.insert(num);
        }
        return false;
    }
}
