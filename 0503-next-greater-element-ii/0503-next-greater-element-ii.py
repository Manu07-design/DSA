class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(2*n):
            current = nums[i%n]
            while stack and current > nums[stack[-1]]:
                index = stack.pop()
                ans[index] = current
            if i<n:
                stack.append(i)
        return ans