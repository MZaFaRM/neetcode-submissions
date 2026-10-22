from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for string in strs:
            reprs = [0] * 26
            for char in string:
                reprs[ord('a') - ord(char)] += 1
            
            hash_map[tuple(reprs)].append(string)

        return list(hash_map.values())