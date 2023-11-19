class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        numbers=sorted(numbers)
        output=[]
        i=0
        j=len(numbers)-1
        while i<j:
            k=numbers[i]+numbers[j]
            if k==target:
                output.append(i+1)
                output.append(j+1)
                return output
            if k<target:
                i=i+1
            else:
                j=j-1