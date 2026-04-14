class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = {}

        for i in range(len(strs)):

            key = [0]* 26
            for letter in strs[i]:
                key[ord(letter) - ord('a')] += 1
            
            tup_key = tuple(key)

            if tup_key in table:
                table[tup_key].append(strs[i])
            else:
                table[tup_key] = [strs[i]]

        return [value for value in table.values()]
