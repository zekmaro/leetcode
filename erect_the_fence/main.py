from typing import List

class Solution:
	def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
		def orientation(p, q, r):
			return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

		def build(points):
			hull = []
			for p in points:
				while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) <= 0:
					hull.pop()
				hull.append(p)
			return hull

		trees.sort()
		return build(trees) + build(trees[::-1])[1:-1]