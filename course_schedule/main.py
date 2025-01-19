from typing import List

class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		stack = []
		recStack = []

		def build_adj_list():
			adj_list = {i: [] for i in range(numCourses)}
			for dest, source in prerequisites:
				if source not in adj_list:
					adj_list[source] = []
				adj_list[source].append(dest)
				if dest not in adj_list:
					adj_list[dest] = []
			return adj_list
		
		adj_list = build_adj_list()

		def dfs():
			visited = set()

			def visit(node):
				if node in recStack:
					return False
				if node in visited:
					return True
				recStack.append(node)
				visited.add(node)
				for neighbor in adj_list[node]:
					if not visit(neighbor):
						return False
				stack.append(node)
				recStack.pop()
				return True

			for node in adj_list:
				if node not in visited:
					if not visit(node):
						return False

			if len(stack) != numCourses:
				return False
			return True

		# print(dfs())
		return dfs()
			

Solution().canFinish(1, [])