# Determines the maximum possible volume of a square with the varying heights in an array, and the varying base widths (the difference between two index values in the array of heights)

class Solution(object):
    def __init__(self):
        self.max_height = 0
        self.max_height_index = None
        self.max_vol = 0
        self.secondary_height = 0
        self.secondary_height_index = None
        self.base_width = 0

    def maxArea(self, heights_array):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # First, find the max height out of the avaiable indicies in the array
        for i in range(len(heights_array)):
            if heights_array[i] > self.max_height:
                self.max_height = heights_array[i]
                self.max_height_index = i

        # Then, calculate which value in the array forms the largest volume with the maximum height
        for i in range(len(heights_array)):
            if i != self.max_height_index and (heights_array[i] * (abs(i - self.max_height_index))) >= self.max_vol:
                self.max_vol = (heights_array[i] * (abs(i - self.max_height_index)))
                self.secondary_height = heights_array[i]
                self.secondary_height_index = i
                self.base_width = abs(i - self.max_height_index)

        return "Max Volume: {0} \nWidth x Height: ({1} x {2}) \nBase Indices: ({3}, {4})".format(self.max_vol, self.base_width, self.secondary_height, self.max_height_index, self.secondary_height_index)
        

sol = Solution()

ha1 = [1,8,6,2,5,4,8,3,7]
ha2 = [1,1]

print(sol.maxArea(ha1))