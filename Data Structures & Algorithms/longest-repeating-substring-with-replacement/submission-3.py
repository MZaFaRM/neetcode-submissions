from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:            
        i, j, n, L = 0, 1, len(s), s[0]
        if n == 1:
            return 1

        lens = defaultdict(int)
        lens[L] = 1
        result = 1

        while j < n:
            a, b = s[i], s[j]
            lens[b] += 1
            if lens[b] > lens[L]:
                L = b

            length = j - i + 1
            extra = length - lens[L]  - k

            if extra > 0:
                i += 1
                lens[a] -= 1
            elif length > result:
                result = length
            j += 1
        return result
