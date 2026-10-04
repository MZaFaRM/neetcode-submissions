class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            hash_table = [0] * 26
            for letter in string:
                if letter:
                    # all lowercase letters, hence 97
                    index = ord(letter) - 97
                    hash_table[index] += 1

            hash_table = tuple(hash_table)
            if hash_table not in hash_map:
                hash_map[hash_table] = [string]
            else:
                hash_map[hash_table].append(string)

        return list(hash_map.values())

            

                

            
        