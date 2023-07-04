class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r = 0, len(height) - 1
        maxarea = 0

        while l < r:
            area = min(height[l],height[r]) * (r-l)
            maxarea = max(maxarea,area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:             #If the two heights are equal
                r -= 1
        
        return maxarea