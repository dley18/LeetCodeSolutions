class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            A, B = nums1, nums2
            if len(B) < len(A):
                A, B = B, A

            l, r = 0, len(A) - 1
            total = len(A) + len(B)
            half = total // 2

            while True:
                aMid = (l + r) // 2
                bMid = half - aMid - 2

                aLeft = A[aMid] if aMid >= 0 else float("-inf")
                aRight = A[aMid + 1] if aMid + 1 < len(A) else float("inf")
                bLeft = B[bMid] if bMid >= 0 else float("-inf")
                bRight = B[bMid + 1] if bMid + 1 < len(B) else float("inf")

                if aLeft <= bRight and bLeft <= aRight:
                    if total % 2:
                        return min(aRight, bRight)
                    else:
                        return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                elif aLeft > bRight:
                    r = aMid - 1
                else:
                    l = aMid + 1 