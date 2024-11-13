class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spl = s.split()
        return len(spl[-1])
    
sol = Solution()
print(sol.lengthOfLastWord('Hello World'))