# Write a function that takes in a non-empty array of integers that are sorted in ascending order and 
# returns a new array of the same length with the squares of the original integers also sorted in ascending order.
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
# print(result)


# practice
def practice1(array):
    newArr = [ 0 for _ in array]
    left = 0
    right = len(array) -1
    for i in reversed(range(len(array))):


        absLeftVal = abs(array[left])
        absRightVal = abs(array[right])
        print(absLeftVal,absRightVal)

        if absLeftVal > absRightVal:
            newArr[i] = absLeftVal*absLeftVal
            left +=1
        else:
            newArr[i] = absRightVal * absRightVal
            right -=1
    return newArr
input = [-10, -5, 0, 5, 10]
result1 = practice1(input)
print(result1)
