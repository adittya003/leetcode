import sys
def doSomething(list_val,k,n):
    beauty_array=[]
    for i in range(len(list_val)-k+1):
        subarray=list_val[i:i+k]
        sorted_subarray=sorted(subarray)
        beauty_array.append(sorted_subarray[n-1])
    
    return beauty_array
inputVal = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8, 9 ,10]
k=3
n=2
outputVal = doSomething(inputVal,k,n)
print (outputVal)

inputVal = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8, 9 ,10]
k=4
n=2
outputVal = doSomething(inputVal,k,n)
print (outputVal)