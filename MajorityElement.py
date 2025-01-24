class Solution(object):
    
    def __init__(self):
        # Dictionary to maintain a tally of how many times each integer appears in the array (value : number of appearances)
        self.seen_values = {}
        self.majority_element = None

    def majorityElement(self, nums):

        # Populate the dictionary with the integers (keys) and the number of times they are seen (values)
        for i in nums:
            if i not in self.seen_values:
                # First time seeing said integer, tally one
                self.seen_values[i] = 1
            else:
                # Seen integer earlier in the array, increment tally by one
                self.seen_values[i] = self.seen_values[i] + 1

        num_values = len(nums)

        draw_element = None
        draw_tally = 0
        max_tally = 0

        # Look through the dictionary for the higher tally number
        for i in self.seen_values:

            # Indicates a majority element by default, no need to look further (nums1 and nums2)
            if self.seen_values[i] > num_values/2:
                self.majority_element = i
                return "majority element: {0}".format(self.majority_element)
            
            # Keeps track of the max tally seen in the dictionary and its key (nums4)
            elif self.seen_values[i] > max_tally:
                max_tally = self.seen_values[i]
                self.majority_element = i

            # Indicates a draw between 2 integers among only 2 integers in the array (nums3)
            elif self.seen_values[i] == max_tally and self.seen_values[i] == num_values/2:
                draw_element = i
                draw_tally = max_tally
                return "draw between {0} and {1}".format(self.majority_element, draw_element)
            
            # Indicates a draw between 2 integers exists, but there are integers other than the two drawing integers in the array
            elif self.seen_values[i] == max_tally and self.seen_values[i] < num_values/2:
                draw_element = i
                draw_tally = max_tally

        # If the tally at the point a draw was detected is less than the max tally, this indicates another integer in the array has the majority (nums5)
        if draw_tally < max_tally:
            return "majority element: {0}".format(self.majority_element)
        
        # If the draw tally equals the max tally, this indicates that a draw exists between 2 integers in the array, and there is a minority of other integers in the array (nums6)
        else:
            return "draw between {0} and {1}".format(self.majority_element, draw_element)
        
        
nums1 = [3,2,3] # Simple majority case between 2 integers case
nums2 = [2,2,1,1,1,2,2] # Simple majority case between 2 integers case
nums3 = [2,2,2,4,4,4] # Draw between exclusively two integers case
nums4 = [1,1,1,1,3,3,2,2,4] # Majority integer less than total number of integers case
nums5 = [1,1,1,2,2,2,3,3,3,3] # Draw between two minority integers, and a majority among a single integer case
nums6 = [1,1,1,2,2,2,3,3] # Draw between two majority integers, and a minority integer exisiting in the array case

sol = Solution()

print(sol.majorityElement(nums4))