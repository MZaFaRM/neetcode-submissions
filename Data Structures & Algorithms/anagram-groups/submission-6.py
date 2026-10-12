class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            char_map = [0] * 26
            for char in string:
                char_map[ord(char) - 97] += 1
            char_tuple = tuple(char_map)
            if char_tuple not in groups:
                groups[char_tuple] = []
            groups[char_tuple].append(string)
        return list(groups.values())