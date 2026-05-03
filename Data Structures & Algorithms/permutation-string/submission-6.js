class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length > s2.length) { return false; }

        let s1Count = new Array(26).fill(0);
        let s2Count = new Array(26).fill(0);

        for (let i = 0; i < s1.length; i++) {
            s1Count[s1[i].codePointAt(0) - 'a'.codePointAt(0)] += 1;
            s2Count[s2[i].codePointAt(0) - 'a'.codePointAt(0)] += 1;
        }

        let matches = 0;
        for (let i = 0; i < 26; i++) {
            s1Count[i] === s2Count[i] ? matches += 1 : matches += 0;
        }

        let l = 0;
        for (let r = s1.length; r < s2.length; r++) {
            if (matches === 26) { return true; }

            let index = s2[r].codePointAt(0) - 'a'.codePointAt(0);
            s2Count[index] += 1;

            if (s1Count[index] === s2Count[index]) {
                matches += 1;
            } else if (s1Count[index] + 1 === s2Count[index]) {
                matches -= 1;
            }

            index = s2[l].codePointAt(0) - 'a'.codePointAt(0);
            s2Count[index] -= 1;

            if (s1Count[index] == s2Count[index]) {
                matches += 1;
            } else if (s1Count[index] - 1 === s2Count[index]) {
                matches -= 1;
            }

            l += 1;
        }
        return matches === 26;
    }
}
