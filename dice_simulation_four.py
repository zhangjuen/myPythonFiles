import numpy as np
Result = np.zeros([20])
#non, 1234,3456,3,4,5,6,7,8,9,10,11,12,3same,4same
testNum = 100000
x = np.zeros([4, 1])
for test in range(testNum):
    if test % 10000 == 0:
        print(test)
    #for i in range(4):
    #    x[i] = np.random.randint(6, size=1) + 1
    x = np.random.randint(6, size=4) + 1
    y, counts = np.unique(x, return_counts=True)
    l = len(y)
    if l == 4:
        if np.sum(x) == 10:
            Result[1] += 1
        elif np.sum(x) == 18:
            Result[2] += 1
        else:
            Result[0] += 1
    elif l == 3:
        notPair = y[counts == 1]
        p = np.uint16(sum(notPair)).item()
        # print(notPair)
        Result[p] += 1
    elif l == 2:
        if counts[0] == 2:
            p = np.uint16(max(x)*2).item()
            Result[p] += 1
        else:
            Result[13] += 1
    elif l == 1:
        Result[14] += 1
print(Result)
#print(sum(Result))
print('Less than 8:',(sum(Result[3:7])+Result[1])/testNum*100)
#print((sum(Result[3:7])+Result[1])/testNum*100)
print('Equal tp 8:',Result[8]/testNum*100)
#print(Result[8]/testNum*100)
print('More than 8:',(sum(Result[9:14])+Result[2])/testNum*100)
#print((sum(Result[9:14])+Result[2])/testNum*100)
print('non result:',Result[0]/testNum*100)
#print(Result[0]/testNum*100)
