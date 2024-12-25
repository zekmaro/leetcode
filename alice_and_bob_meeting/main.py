class Solution(object):


	def find_next_greater_index(self, source, heights, tree, qs, qe, start, end, node):
		if start > qe or end < qs:
			return -1

		if start == end:
			if heights[start] > source:
				return start
			return -1

		index_max_value = self.find_index_max_value_in_range(heights, tree, qs, qe, start, end, node)
		if index_max_value == -1 or heights[index_max_value] <= source:
			return -1

		mid = (start + end) // 2

		result = self.find_next_greater_index(source, heights, tree, qs, qe, start, mid, node * 2)
		if result != -1:
			return result

		return self.find_next_greater_index(source, heights, tree, qs, qe, mid + 1, end, node * 2 + 1)
			

	def find_index_max_value_in_range(self, heights, tree, qs, qe, start, end, node):

		if start > qe or end < qs:
			return -1

		if start >= qs and end <= qe:
			return tree[node]

		mid = (start + end) // 2
		max_left = self.find_index_max_value_in_range(heights, tree, qs, qe, start, mid, node * 2)
		max_right = self.find_index_max_value_in_range(heights, tree, qs, qe, mid + 1, end, node * 2 + 1)

		if max_left == -1:
			return max_right
		if max_right == -1:
			return max_left
		return max_left if heights[max_left] > heights[max_right] else max_right


	def build_range_max_tree(self, heights, tree, start, end, node):
		if (start == end):
			tree[node] = start
			return
		
		mid = (start + end) // 2
		self.build_range_max_tree(heights, tree, start, mid, node * 2)
		self.build_range_max_tree(heights, tree, mid + 1, end, node * 2 + 1)

		left_child_index = tree[node * 2]
		right_child_index = tree[node * 2 + 1]
		if (heights[left_child_index] > heights[right_child_index]):
			parent_node = left_child_index
		else:
			parent_node = right_child_index
		tree[node] = parent_node


	def leftmostBuildingQueries(self, heights, queries):
		ans = []
		list_length = len(heights)
		tree = [-1] * 4 * (list_length + 1)
		self.build_range_max_tree(heights, tree, 0, list_length - 1, 1)
		for query in queries:
			a = query[0]
			b = query[1]
			if a > b:
				temp = b
				b = a
				a = temp
			if a == b:
				ans.append(a)
			elif heights[b] > heights[a]:
				ans.append(b)
			else:
				if (b == list_length - 1):
					b -= 1
				next_greater_index = self.find_next_greater_index(heights[a], heights, tree, b + 1, list_length - 1, 0, list_length - 1, 1)
				ans.append(next_greater_index)
		return ans
			

solution = Solution()
heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
ans = solution.leftmostBuildingQueries(heights, queries)
print(ans)