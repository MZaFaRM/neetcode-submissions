class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_tables = {}
        for string in strs:
            hash_table = [0] * 26
            for letter in string:
                if letter:
                    # all lowercase letters, hence 97
                    index = ord(letter) - 97
                    hash_table[index] += 1

            hash_table = tuple(hash_table)
            if hash_tables.get(hash_table, None) is None:
                hash_tables[hash_table] = [string]
            else:
                hash_tables[hash_table].append(string)

        return list(hash_tables.values())

            

                

            
        