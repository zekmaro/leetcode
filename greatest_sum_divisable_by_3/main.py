from typing import List

class Solution:
	def maxSumDivThree(self, nums: List[int]) -> int:
		total = sum(nums)
		r = total % 3
		if r == 0:
			return total

		bucket1 = []
		bucket2 = []

		for num in nums:
			if num % 3 == 1:
				bucket1.append(num)
			elif num % 3 == 2:
				bucket2.append(num)

		bucket1.sort()
		bucket2.sort()

		# We will compare candidates
		candidates = []

		if r == 1:
			if bucket1:
				candidates.append(bucket1[0])
			if len(bucket2) >= 2:
				candidates.append(bucket2[0] + bucket2[1])

		else:  # r == 2
			if bucket2:
				candidates.append(bucket2[0])
			if len(bucket1) >= 2:
				candidates.append(bucket1[0] + bucket1[1])

		if not candidates:
			return 0

		return total - min(candidates)
