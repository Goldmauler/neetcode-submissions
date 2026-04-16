class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(257)
        res = ""
        for s in strs:
            res += str(len(s)) + ","
        res += "#"
        for s in strs:
            res += s
        return res


    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res