'''nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

l = 1

for r in range(1, len(nums)):
    if nums[r] != nums[r-1]:
        nums[l] = nums[r]
        l += 1

print(l, nums)'''


class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l


# Here two pointer is used to track and check for duplicate
# l and r
# l hold the initialized position while r travarse through the list, when it finds unique element
# by checking r position with it's previous position then replace the l position with r value and increment l
p1 = Solution()
print(p1.removeDuplicates([]))
# print(p1.removeDuplicates(i // 2 for i in range(10)))
# print(p1.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(p1.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(p1.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
