#this algorithm is kinda alike with binary search
#i dont understand one point, why do they return the left variable

class Solution:
    def Search_Insert_Position(nums, target):
        left = 0
        right = len(nums)
        while left <= right and left < len(nums) and right >= 0:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

nums = [1, 3, 4, 5, 6, 7, 20, 45, 200, 4000]
target = 25
print(Solution.Search_Insert_Position(nums, target))