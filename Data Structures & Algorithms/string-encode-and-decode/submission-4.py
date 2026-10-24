class Solution:
    dm = "."

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            n = f"{self.dm}{len(string)}{self.dm}"
            result.extend([n, string])
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        start = 1
        n = len(s)
        strs = []
        end = 1

        while end < n:
            end += 1
            while s[end] != self.dm:
                end += 1
            length = int(s[start:end])
            start = end = end + 1
            
            end += length
            strs.append(s[start:end])
            start = end = end + 1
            
        return strs
