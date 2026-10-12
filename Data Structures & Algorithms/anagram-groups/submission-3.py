class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        seen = {}
        n = 0
        for string in strs:
            ordered_string = tuple(sorted(string))
            if ordered_string in seen:
                index = seen[ordered_string] 
            else:
                seen[ordered_string] = n
                index = n
                n += 1
                groups.append([])
            groups[index].append(string)
        return groups
