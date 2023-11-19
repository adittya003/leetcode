class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict1={}
        nums=sorted(nums)
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1

        l1=[]

    # dict1.items() converts the dictionary into a list of tuples.
    # key=lambda x: x[1] specifies that the sorting should be based on the second         element   (value) of each tuple.
    # reverse=True ensures the list is sorted in descending order based on the value
        dict1=sorted(dict1.items(),key=lambda x: x[1],reverse=True)
        for i in range(k):
            l1.append(dict1[i][0])
            
        return l1
            