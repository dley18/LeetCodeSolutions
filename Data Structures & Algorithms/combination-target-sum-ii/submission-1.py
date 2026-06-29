class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        candidates.sort()

        def dfs(idx: int, total: int):
            if total == target:
                res.append(combo.copy())
                return

            if total > target:
                return

            if idx >= len(candidates):
                return

            combo.append(candidates[idx])
            total += candidates[idx]
            dfs(idx + 1, total)

            old_idx = idx
            while idx < len(candidates) and candidates[old_idx] == candidates[idx]:
                idx += 1

            total -= combo.pop()
            dfs(idx, total)

        dfs(0, 0)
        return res