from typing import List

class Solution:
	
	def minCost(self, n: int, cuts: List[int]) -> int:
		hash_map = {}
		
		def dfs(l, r):
			if r - l == 1:
				return 0
			if (l, r) in hash_map:
				return hash_map[(l,r)]

			res = float("inf")
			for cut in cuts:
				if l < cut < r:
					res = min(
						res,
						(r - l) + dfs(l, cut) + dfs(cut, r)
					)
			if res == float("inf"):
				res = 0
			hash_map[(l,r)] = res
			return res

		return dfs(0, n)
