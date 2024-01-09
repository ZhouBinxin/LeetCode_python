class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        arab = 0
        prev_value = 0

        for i in range(len(s)):
            current_value = roman_dict[s[i]]
            if current_value > prev_value:
                arab += current_value - 2 * prev_value
            else:
                arab += current_value
            prev_value = current_value

        return arab


solution = Solution()
s = "IV"
result = solution.romanToInt(s)
print(result)
