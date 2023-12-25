class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if tomatoSlices % 2 != 0:
            return []
        total_jumbo = tomatoSlices / 2 - cheeseSlices
        if total_jumbo < 0:
            return []
        total_small = cheeseSlices - total_jumbo
        if total_jumbo * total_small < 0:
            return []
        return [int(total_jumbo), int(total_small)]


solution = Solution()

tomatoSlices = 16
cheeseSlices = 7
result = solution.numOfBurgers(tomatoSlices, cheeseSlices)
print(result)
