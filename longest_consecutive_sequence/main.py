from typing import List


class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		numset = set(nums)
		longest = 0

		for x in numset:
			if x - 1 not in numset:
				length = 1
				y = x + 1
				while y in numset:
					length += 1
					y += 1
				longest = max(longest, length)
		
		return longest
			
sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))
