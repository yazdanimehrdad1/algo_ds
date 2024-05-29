"""
O(n^2) time | O(1) space
"""
array= [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10

def two_number_sum(array, target_sum):
    for i in range(len(array)-1):
        first_num = array[i]
        for j in range(i+1 , len(array)):
            second_num = array[j]
            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []

"""
O(n) time | O(n) space
"""
def two_number_sum_2(array, target_sum):
    nums = {}
    for num in array:
        potential_match = target_sum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return []

"""
O(nlog(n)) time | O(1) space
"""
def two_number_sum3(array, target_sum):
    array.sort()
    left = 0
    right = len(array)-1
    while left< right:
        current_sum = array[left]+ array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left+=1
        elif current_sum > target_sum:
            right -=1
    return []



#practice
def sum_function(array, target):
    array.sort()
    left = 0 
    right = len(array) -1
    while left < right:
        currentSum = array[left] + array[right]


        if currentSum< target:
            left +=1
        elif currentSum> target:
            right -=1
        else:
            return [array[left], array[right]]
    return []
        

print(sum_function(array, target_sum))          