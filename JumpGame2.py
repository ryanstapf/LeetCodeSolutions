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
            
            elif jump_counter > last_index:
                return False
            
            elif nums[jump_counter] == 0:
                return jump_counter
        
nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
nums3 = [2,3,0,1,4]
nums4 = [2,3,4,0,1]

sol = Solution()

print(sol.canJump(nums4))