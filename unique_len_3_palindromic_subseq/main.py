class Solution:
	def countPalindromicSubsequence(self, s: str) -> int:
		polyndroms = set()
		left = set()
		right = {}

		for c in s:
			if c not in right:
				right[c] = 1
			else:
				right[c] += 1

		for m in s:
			right[m] -= 1
			for c in left:
				if right[c] > 0:
					polyndroms.add((c, m))
			left.add(m)
		
		return len(polyndroms)


sol = Solution()
s = "aabca"
print(sol.countPalindromicSubsequence(s))
