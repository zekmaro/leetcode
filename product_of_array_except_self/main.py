from typing import List


class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		left = [0] * len(nums)
		right = [0] * len(nums)
		res = [0] * len(nums)

		left[0] = nums[0]
		right[-1] = nums[-1]

		for i in range(1, len(nums)):
			left[i] = left[i - 1] * nums[i]
			right[len(nums) - 1 - i] = right[len(nums) - i] * nums[len(nums) - 1 - i]
		
		res[0] = right[1]
		res[-1] = left[-2]

		for i in range(1, len(nums) - 1):
			res[i] = left[i - 1] * right[i + 1]
		
		return res

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
