from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max1 = score = float('-inf')
        for i in range(1, len(values)):
            max1 = max(max1, values[i - 1] + i - 1)
            score = max(score, max1 + values[i] - i)
        return score

solution = Solution()
values = [8,1,5,2,6]
score = solution.maxScoreSightseeingPair(values)
print(score)