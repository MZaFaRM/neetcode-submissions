class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + '_' + string + '_'
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)

        length = 0
        length_str = ''

        output = []
        while i < n:
            if s[i] == '_':
                length = int(length_str)
                i += 1
                output.append(s[i:i+length])
                i += length + 1
                length_str = ""
            else:
                length_str += s[i]
                i += 1
        return output