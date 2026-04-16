class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        P = len(potions)
        ans = []
        for spell in spells:
            now = len(potions) - bisect_left(potions,success/spell)
            ans.append(now)
        return ans
