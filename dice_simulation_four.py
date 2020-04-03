import numpy as np
Result = np.zeros([20, 1])
#non, 1234,3456,3,4,5,6,7,8,9,10,11,12,3same,4same
testNum = 100000
x = np.zeros([4, 1])
for test in range(testNum):
    if test % 1000 == 0:
        print(test)
    for i in range(4):
        x[i][0] = np.random.randint(6, size=1) + 1
    y, counts = np.unique(x, return_counts=True)
    l = len(y)
    if l == 4:
        if np.sum(x) == 10:
            Result[1][0] += 1
        elif np.sum(x) == 18:
            Result[2][0] += 1
        else:
            Result[0][0] += 1
    elif l == 3:
        notPair = y[counts == 1]
        p = np.uint16(sum(notPair)).item()
        # print(notPair)
        Result[p][0] += 1
    elif l == 2:
        if counts[0] == 2:
            p = np.uint16(max(x)*2).item()
            Result[p][0] += 1
        else:
            Result[13][0] += 1
    elif l == 1:
        Result[14][0] += 1
print(Result)

print((np.sum(Result[3:7][0])+Result[1][0])/test*100)
print((np.sum(Result[9:14][0])+Result[2][0])/test*100)
