class Solution:
    def maxArea(self, height: list[int]) -> int:
        j=len(height)-1
        i=0
        max_area=0

        while i<j:
            width=j-i
            container_height=min(height[i],height[j])
            area=width*container_height
            max_area=max(area,max_area)
        
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

                
