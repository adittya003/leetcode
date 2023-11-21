def doSomething(num, k):
    if num==0:
        return -1
    sum=0
    ans=-1
    for i in range(0,10):
        sum+=k
        if (sum%10 == num%10):
            ans=i+1
            break
    
    if ans== -1 or ans*k>num:
        return -1
    
    return ans
    

# Example usage:
print(doSomething(56, 9))
print(doSomething(53, 9))