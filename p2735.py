class Solution(object):
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        minCost = [float('inf')] * len(nums)
        n = len(nums)
        result = float('inf')
        for i in range(n):
            temp_sum = i * x
            for j in range(n):
                site = (j + n - i) % n
                minCost[j] = min(minCost[j], nums[site])
                temp_sum += minCost[j]

            result = min(result, temp_sum)

        return result


solution = Solution()

nums = [20, 1, 15]
x = 5
result = solution.minCost(nums, x)
print(result)

nums = [1, 2, 3]
x = 4
result = solution.minCost(nums, x)
print(result)
