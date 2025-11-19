from typing import List


class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		num_to_freq = {}
		res = []
		for num in nums:
			if num not in num_to_freq.keys():
				num_to_freq[num] = 1
			else:
				num_to_freq[num] += 1

		buckets = [[] for _ in range(len(nums) + 1)]

		for num, freq in num_to_freq.items():
			buckets[freq].append(num)

		res = []
		for i in range(len(buckets) - 1, 0, -1):
			for num in buckets[i]:
				if len(res) == k:
					break
				res.append(num)

			if len(res) == k:
				break	

		return res

res = Solution()
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(res.topKFrequent(nums, k))