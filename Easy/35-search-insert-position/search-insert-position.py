class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i=0
        j=len(nums)-1

        while i<=j:
            mid =(i+j)//2
            if target < nums[mid]:
                j = mid-1   
            elif target > nums[mid]:
                i= mid+1
            else:
                return mid

        return i
