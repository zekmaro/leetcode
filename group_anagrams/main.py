from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for s in strs:
            s_ = tuple(sorted(s))
            ht.setdefault(s_, []).append(s)
        return list(ht.values())