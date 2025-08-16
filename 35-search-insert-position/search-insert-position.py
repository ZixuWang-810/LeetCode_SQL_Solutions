class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        if target < nums[left]: return left
        elif target > nums[right]: return right+1
        else:
            while left <= right: 
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return left