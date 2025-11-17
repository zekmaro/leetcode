from typing import List


class Solution:
	def kLengthApart(self, nums: List[int], k: int) -> bool:
		last = -1
		for i, num in enumerate(nums):
			if num == 1:
				if last != -1 and i - last - 1 < k:
					return False
				last = i
		return True

sol = Solution()
arr = [1,0,0,1,0,1]
k = 2
print(arr)
print(sol.kLengthApart(arr, k))
