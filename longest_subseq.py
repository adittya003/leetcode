import sys
def doSomething(inval):
    char=set()
    max_length=0
    length=0
    for i in inval:
        if i not in char:
            char.add(i)
            length+=1
        else:
            max_length=max(max_length,length)
            char.clear()
            char.add(i)
            length=1

    max_length=max(max_length,length)
    return max_length

inputVal1 = "pqrsstu"    
outputVal1 = doSomething(inputVal1)
print (outputVal1)

inputVal2 = "abbedfgi"    
outputVal2 = doSomething(inputVal2)
print (outputVal2)