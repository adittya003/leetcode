#time exceeded error
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        product=[1]*n
        for i in range(n):
            for j in range(0,n):
                if j!=i:
                    product[i]=nums[j]*product[i]
                else:
                    continue
        return product
    
class Solution1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
       
        answer = [1] * n
        
        
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
