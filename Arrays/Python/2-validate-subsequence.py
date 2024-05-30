"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. 
For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] , and so do the numbers [2, 4] . 
Note that a single number in an array and the array itself are both valid subsequences of the array.

Input: 
array:[5,1,22,25,6,-1, 8,10]
sequence:[1, 6 , -1, 10]
output:
true
"""
"""
O(n) time | O(1) space
"""
def isValidSubsequence(array,subseq):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(seqIdx):
        if array[arrIdx] == subseq[seqIdx]:
            seqIdx +=1
        arrIdx+=1
    return seqIdx == len(subseq)

"""
O(n) time | O(1) space
"""
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if value == sequence[seqIdx]:
            seqIdx += 1
        if seqIdx == len(sequence):
            break
    return seqIdx == len(sequence)


#Practice1
array= [5,1,22,25,6,-1, 8,10]
sequence=[1, 6 , -1, 10]
def practice1(array, sequence):
    seqIdx = 0
    for arrIdx in range(len(array)):
        arrValue = array[arrIdx]
        if arrValue == sequence[seqIdx]:
            seqIdx +=1
    return seqIdx == len(sequence)

def practice2(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx +=1
        arrIdx +=1
    return seqIdx == len(sequence)



array:[5,1,22,25,6,-1, 8,10]
sequence:[1, 6 , -1, 10]
result1 = practice1(array, sequence)
print(result1)
