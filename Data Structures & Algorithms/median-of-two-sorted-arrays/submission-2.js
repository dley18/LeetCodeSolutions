class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
        let A = nums1;
        let B = nums2;

        if (B.length < A.length) {
            A = nums2;
            B = nums1;
        }

        let l = 0;
        let r = A.length - 1;
        const total = A.length + B.length;
        const half = Math.floor(total / 2);

        while (true) {
            let aMid = Math.floor((l + r) / 2);
            let bMid = half - aMid - 2;

            let aLeft = aMid >= 0 ? A[aMid] : -Infinity;
            let aRight = aMid + 1 < A.length ? A[aMid + 1] : Infinity;
            let bLeft = bMid >= 0 ? B[bMid] : -Infinity;
            let bRight = bMid + 1 < B.length ? B[bMid + 1] : Infinity;

            if (aLeft <= bRight && bLeft <= aRight) {
                if (total % 2) {
                    return Math.min(aRight, bRight);
                } else {
                    return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2;
                }
            } else if (aLeft > bRight) {
                r = aMid - 1;
            } else {
                l = aMid + 1;
            }
        }
    }
}
