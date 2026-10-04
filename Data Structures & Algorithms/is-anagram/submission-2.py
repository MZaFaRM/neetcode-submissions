class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = {}
        flags = 0

        for letter in s:
            if hash_table.get(letter, None) is None:
                hash_table[letter] = 1
                flags += 1
            else:
                hash_table[letter] += 1

        for letter in t:
            if not hash_table.get(letter, 0):
                return False
            else:
                hash_table[letter] -= 1
                if hash_table[letter] == 0:
                    flags -= 1
        return flags <= 0
        