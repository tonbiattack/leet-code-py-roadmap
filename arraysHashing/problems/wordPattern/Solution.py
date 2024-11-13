class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = []
        map2 = []
        for idx in pattern:
            map1.append(pattern.index(idx))
        s = s.split()
        for idx in s:
            map2.append(s.index(idx))
        if map1 == map2:
            return True
        return False


sol = Solution()
# print(sol.isIsomorphic("egg", "add"))
print(sol.wordPattern("abba", "dog cat cat dog"))