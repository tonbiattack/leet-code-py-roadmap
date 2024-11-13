class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
    

# 呼び出し箇所
if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    sol = Solution()
    print(sol.mergeAlternately(word1, word2))
    
    word1 = "ab"
    word2 = "pqrs"
    print(sol.mergeAlternately(word1, word2))
    
    word1 = "abcd"
    word2 = "pq"
    print(sol.mergeAlternately(word1, word2))
    