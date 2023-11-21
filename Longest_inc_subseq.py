class Solution:
    def LIS(self, nums: list[int]) -> list:
        # Initialize LIS lengths with 1
        L = [1] * len(nums)
        
        for i in range(1, len(L)):
            # Construct a list of LIS lengths for indices k less than i where nums[k] < nums[i]
            subproblem = [L[k] for k in range(i) if nums[k] < nums[i]]

# subproblem = []


# for k in range(i):
#     # Check if the element at index k is less than the element at index i
#     if nums[k] < nums[i]:
#         subproblem.append(L[k])

            
            # Update LIS length at index i based on the subproblem
            L[i] = 1 + max(subproblem, default=0)
        
        return L

# Create an instance of the Solution class
solution = Solution()

# Example usage: Call the LIS function with the provided list
num = [3, 1, 8, 2, 5]
result = solution.LIS(num)

# Print the result
print(result)
