array= [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum1(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            sum = array[i]+array[j]
            if targetSum == sum:
                return [array[i],array[j]]
    return None

twoNumberSum1Result = twoNumberSum1(array,targetSum)
print(twoNumberSum1Result)


def twoNumberSum2(array, targetSum):
    memory = {}
    for i in range(len(array)):
        num1 = array[i]
        complement1 = targetSum - num1
        if  complement1 in memory: 
            return [num1, complement1]
        else:
            memory[num1]= True
    return None


twoNumberSum2Result = twoNumberSum2(array,targetSum)
print(twoNumberSum2Result)

def twoNumberSum3(array, targetSum):
    leftidx =0
    rightidx = len(array)-1
    array.sort()
    while leftidx<rightidx:

        currSum = array[leftidx]+array[rightidx]
        if currSum < targetSum: 
            leftidx+=1
        elif currSum> targetSum:
            rightidx -=1
        else:
            return [array[leftidx], array[rightidx]]

    return None


twoNumberSum3Result = twoNumberSum3(array,targetSum)
print(twoNumberSum3Result)

def isValidSubsequence(array, subseq):
    arrIdx = 0
    seqIdx = 0
    
    while seqIdx < len(subseq) and arrIdx< len(array):

        if array[arrIdx] == subseq[seqIdx]:
            seqIdx+=1
        else:
            arrIdx+=1
    if seqIdx == len(subseq)-1:
        return True
    else: 
        return False
        
