def clumsy(N):
        cl = ""
        ops = ["*", "/", "+", "-"]
        op = 0
        for n in range(N, 0, -1):
            if n != 1:
                cl += str(n) + ops[op % 4]
            else:
                cl += "1"
            op += 1
        return eval(cl)//1

inputVal = 5
outputVal = clumsy(inputVal)
print(outputVal)