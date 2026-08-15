class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = r

        def binary_search(l: int, r: int) -> int:
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        res_left = binary_search(0, pivot - 1)
        res_right = binary_search(pivot, len(nums) - 1)

        if res_left != -1:
            return res_left
        elif res_right != -1:
            return res_right
        else:
            return -1
        