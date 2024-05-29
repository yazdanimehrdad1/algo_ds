# input is sorted array of integers but keep in mind that they could be negative too
"""
input = [1, 2, 3, 5, 6, 8, 9]
expected = [1, 4, 9, 25, 36, 64, 81]
"""


"""
O(nlog(n)) time | O(1) space
"""
def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] = array[i]*array[i]
    array.sort()
    return array
"""
O(n) time | O(n) space

"""
def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [ 0 for _ in array]
    smallerValIdx = 0
    largerValIdx = len(array)-1
    for i in range(len(array)):
        print(len(array)-1-i)
        smallerVal = array[smallerValIdx]
        largerVal = array[largerValIdx]
        # print([smallerVal, largerVal])

        if abs(smallerVal) > abs(largerVal):
            sortedSquares[len(array)-1-i] = smallerVal*smallerVal
            smallerValIdx +=1
        else:
            sortedSquares[len(array)-1-i] = largerVal*largerVal
            largerValIdx -=1
    return sortedSquares

inputArr = [-10, 2, 3, 5, 6, 8, 9]
result = sortedSquaredArray(inputArr)
print(result)