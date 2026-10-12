from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            char_map = [0] * 26
            for char in string:
                char_map[ord(char) - ord('a')] += 1
            groups[tuple(char_map)].append(string)
        return list(groups.values())