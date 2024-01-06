class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []

        start = 0
        for end in range(1, len(nums)):
            if nums[start] != nums[end]:
                start += 1
                nums[start] = nums[end]

        return start + 1


solution = Solution()

nums = [1, 1, 2]
result = solution.removeDuplicates(nums)
print(result)
