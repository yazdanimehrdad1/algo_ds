"""
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
    while arrIdx < len(array):
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
