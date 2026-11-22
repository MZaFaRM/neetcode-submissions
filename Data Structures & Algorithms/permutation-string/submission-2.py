class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        if m > n:
            return False
        
        freq = [0] * 26
        for char in s1:
            freq[ord(char) - 97] += 1

        i = 0
        for j in range(n):
            index = ord(s2[j]) - 97
            freq[index] -= 1
            if freq[index] == -1:
                while i < n:
                    freq[ord(s2[i]) - 97] += 1
                    i += 1
                    if freq[index] >= 0:
                        break
            else:
                length = j - i + 1
                if length == m:
                    return True
        return False
