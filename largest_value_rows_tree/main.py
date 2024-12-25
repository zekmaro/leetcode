from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
	
	def largestValues(self, root):
		if not root:
			return []
		
		solution = []
		j = 1
		queue = deque([root])
		i = 0
		while queue:
			level_len = len(queue)
			current_max = float('-inf')
			
			for _ in range(level_len):
				current_node = queue.popleft()
				current_max = max(current_max, current_node.val)

				if current_node.left:
					queue.append(current_node.left)
				if current_node.right:
					queue.append(current_node.right)
			
			solution.append(current_max)
		return solution

solution = Solution()

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

largest_values = solution.largestValues(root)
print(largest_values)
