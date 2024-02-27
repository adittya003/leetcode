from itertools import permutations

def min_consecutive_zero(l, k):
    x = '1' * k + '0' * (l - k)
    min_length = 100000

    if k == l:
        min_length = 0
    elif l == 1 and k == 0:
        return 1
    else:
        perm = permutations(x)
        for i in perm:
            mini = 0
            for j in range(len(i)):
                if i[j] == '0':
                    mini += 1
                elif i[j] == '1' and mini != 0:
                    min_length = min(min_length, mini)
                    mini = 0

            # Check after the loop to handle the case where the last character is '0'
            if mini != 0:
                min_length = min(min_length, mini)

    return min_length

