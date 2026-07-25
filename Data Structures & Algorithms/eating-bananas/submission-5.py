class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k: int) -> int:
            total = 0
            for pile in piles:
                hours = pile // k
                if pile % k != 0:
                    hours += 1
                total += hours
            return total

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo



       

        