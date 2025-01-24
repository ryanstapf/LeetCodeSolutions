# Determines which two values in an array add up to a desired result using a hash table

nums1 = [2,7,11,15]
nums2 = [3,2,4]
nums3 = [3,3]

t1 = 9
t2 = 6
t3 = 6

class Solution(object):

    def __init__(self, nums, target):
        self.numsArray = nums
        self.numMap = {}
        self.n = len(nums)
        self.targetVal = target

    def twoSum(self):

        for i in range(self.n):

            complementVal = self.targetVal - self.numsArray[i]

            if complementVal in self.numMap:
                return [i, self.numMap[complementVal]]
            
            self.numMap[self.numsArray[i]] = i

        return "no result"
        

sol = Solution(nums1, t1)

print(sol.twoSum())