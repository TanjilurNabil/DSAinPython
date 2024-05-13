class Solution(object):
    def removeDuplicates(self, nums, val):
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l


p1 = Solution()
print(p1.removeDuplicates([0, 1, 2, 2, 3, 0, 4, 2], 2))
