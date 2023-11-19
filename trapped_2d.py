class Solution:
    def trap(self, height: list[int]) -> int:
        #min(L,R) - H[i]
        n=len(height)
        if n <= 2:
            return 0
        max_left=[0]*n
        max_right=[0]*n
        min_l_and_r=[]
        max_left[0]=height[0]
        max_right[n-1]=height[n-1]
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],height[i])
        
        for i in range(n-2,-1,-1):
            max_right[i]=max(max_right[i+1],height[i])

        for i in range(n):
            min_l_and_r.append(min(max_left[i],max_right[i]))

        sumi=0
        for i in range(n):
            k=max(min_l_and_r[i]-height[i],0)
            sumi+=k
            
        return sumi            
        


        
        