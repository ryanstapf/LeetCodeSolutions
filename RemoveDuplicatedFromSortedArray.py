# Removes duplicates from an array, and performs the operation on the array in-place
# Returns the number of unique integers in the array (k) and a sorted array of non-duplicate integers and '_' strings

class Solution(object):

    def __init__(self):
        self.seenArray = []
        self.k = 0
        self.intArr = []


    def removeDuplicates(self, nums):

        # Check for duplicates in the array
        for i in range(len(nums)):

            # If the integer has not been seen, add it to the seen array
            if nums[i] not in self.seenArray:
                self.seenArray.append(nums[i])

            # If the integer has been seen, replace it with a '_' string
            else:
                nums[i] = '_'

        # Set the value of k to the number of unique integers seen
        self.k = len(self.seenArray)

        # Divide the integers from the '_' strings into another array and sort the integers
        for i in nums:
            if i != '_':
                self.intArr.append(i)
                nums.remove(i)
        self.intArr.sort()

        # Merge the integers back into the original array and return k and the sorted array
        nums = self.intArr + nums

        return "k = {0}".format(self.k), nums
        

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()

print(sol.removeDuplicates(nums2))