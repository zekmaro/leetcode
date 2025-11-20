from typing import List


class Solution:
	def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
		chosen = set()

		intervals.sort(key=lambda x: x[1])
		for nums in intervals:
			count = 0
			for check in chosen:
				if check >= nums[0] and check <= nums[-1]:
					count += 1
			need = 2 - count
			candidate = nums[-1]
			while need > 0:
				if candidate not in chosen:
					chosen.add(candidate)
					need -= 1
				candidate -= 1
		
		return len(chosen)


sol = Solution()
a = [[1,3],[3,7],[8,9]]
b = [[1,3],[1,4],[2,5],[3,5]]
c = [[1,2],[2,3],[2,4],[4,5]]
print(sol.intersectionSizeTwo(c))
