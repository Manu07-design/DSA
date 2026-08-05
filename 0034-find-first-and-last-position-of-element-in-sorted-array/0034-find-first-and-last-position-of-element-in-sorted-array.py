class Solution(object):
    def searchRange(self, nums, target):
        def findfirst():
            left ,right=0,len(nums)-1
            ans =-1
            while left<=right:
                mid = (right+left)//2
                if nums[mid]<target:
                    left = mid+1
                elif nums[mid]>target:
                    right = mid-1
                else:
                   ans = mid
                   right = mid-1
            return ans
        def findlast():
            left ,right=0,len(nums)-1
            ans=-1
            while left<=right:
               mid = (right+left)//2
               if nums[mid]<target:
                   left = mid+1
               elif nums[mid]>target:
                  right = mid-1
               else:
                  ans = mid
                  left = mid+1
            return ans
        return[findfirst(),findlast()]