class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        last_index = len(nums) - 1
        jump_counter = 0

        while True:

            jump_counter = jump_counter + nums[jump_counter]

            if jump_counter == last_index:
                return True
            
            elif (jump_counter > last_index) or (nums[jump_counter] == 0):
                return False
        
nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
nums3 = [2,3,0,1,4]

sol = Solution()

print(sol.canJump(nums3))