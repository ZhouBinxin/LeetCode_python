import heapq


class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        # 转换为最大堆
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            # 执行移除操作
            max_pile = -heapq.heappop(max_heap)
            new_pile = max_pile - max_pile // 2
            heapq.heappush(max_heap, -new_pile)

        # 返回剩余石子的最小总数
        return -sum(max_heap)


solution = Solution()

piles1 = [5, 4, 9]
k1 = 2
print(solution.minStoneSum(piles1, k1))

piles2 = [4, 3, 6, 7]
k2 = 3
print(solution.minStoneSum(piles2, k2))
