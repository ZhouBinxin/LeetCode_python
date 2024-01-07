class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        flag = 0
        for i in range(length - 1, -1, -1):
            if s[i] != ' ':
                flag += 1
            elif flag > 0:
                return flag

        return flag


solution = Solution()

s = "a"
result = solution.lengthOfLastWord(s)
print(result)
