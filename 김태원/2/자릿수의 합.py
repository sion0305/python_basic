import sys
# sys.stdin=open("κΉνμ/input.txt", "rt")

def getSum(n):
    tmp = [int(i) for i in str(n)]
    return sum(tmp)

n = int(input())
a = list(map(int, input().split()))

maxSum = 0
maxNum = 0
for i in a:
    thisSum = getSum(i)
    if maxSum < thisSum:
        maxSum = thisSum
        maxNum = i

print(maxNum)
