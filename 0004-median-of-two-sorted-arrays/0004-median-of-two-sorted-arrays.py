class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        half = (m + n + 1) // 2

        while left <= right:

            partitionA = (left + right) // 2
            partitionB = half - partitionA

            # Left and right values around partition A
            if partitionA == 0:
                Aleft = float("-inf")
            else:
                Aleft = nums1[partitionA - 1]

            if partitionA == m:
                Aright = float("inf")
            else:
                Aright = nums1[partitionA]

            # Left and right values around partition B
            if partitionB == 0:
                Bleft = float("-inf")
            else:
                Bleft = nums2[partitionB - 1]

            if partitionB == n:
                Bright = float("inf")
            else:
                Bright = nums2[partitionB]

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

                # Even total length
                else:
                    left_max = max(Aleft, Bleft)
                    right_min = min(Aright, Bright)

                    return (left_max + right_min) / 2.0

            # Too many elements taken from nums1
            elif Aleft > Bright:
                right = partitionA - 1

            # Too few elements taken from nums1
            else:
                left = partitionA + 1