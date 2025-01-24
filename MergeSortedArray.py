# Merge sort algorithm

class Solution(object):

    def merge(self, nums1, m, nums2, n):

        i = m
        while i < (m + n):
            nums1[i] = nums2[i - m]
            i += 1

        nums1.sort()

        print(nums1)


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

sol = Solution()

sol.merge(nums1, m, nums2, n)