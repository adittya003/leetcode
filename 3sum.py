class brute_force:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums1=sorted(nums)
        s=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if(i!=j and i!=k and j!=k):
                        target=nums1[i]+nums1[j]+nums1[k]
                        if(target==0):
                            s.append([nums1[i],nums1[j],nums1[k]])
        
        unique_s=[]
        for i in s:
            i=sorted(i)
            if i not in unique_s:
                unique_s.append(i)
        return unique_s
    

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        num=sorted(nums)
        result=[]
        n=len(nums)
        for i in range(n-2):
            right=n-1
            left=i+1
            while left<right:
                target=num[i]+num[left]+num[right]
                if target==0:
                    j=sorted([num[i],num[left],num[right]])
                    if j not in result:
                        result.append(j)
                    left=left+1
                    right=right-1
                elif target<0:
                    left=left+1
                else:
                    right=right-1   
        
        return result  

