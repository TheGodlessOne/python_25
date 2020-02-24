def BinarySearchRecursive(array, left, right, x): 
    if right >= left: 
        middle = left + (right - left)/2
        if arr[middle] == x: 
            return middle 
        elif arr[middle] > x: 
            return BinarySearchRecursive(arr, left, middle-1, x) 
        else: 
            return BinarySearchRecursive(arr, middle+1, right, x) 


def BinarySearchIterative(array, left, right, x): 
    while left <= right: 
        middle = left + (right - left)/2; 
        if arr[middle] == x: 
            return middle 
        elif arr[middle] < x: 
            left = middle + 1
        else: 
            right = middle - 1
    return -1


print('Test the empty array:')
arr = [] 
result_rec = BinarySearchRecursive(array, 0, len(arr)-1, x)
result_iter = BinarySearchIterative(array, 0, len(arr)-1, x) 

arr = [i for i in range(20)]
print('Test the non-existing element:')
x = 40
result_rec = BinarySearchRecursive(array, 0, len(arr)-1, x)
result_iter = BinarySearchIterative(array, 0, len(arr)-1, x) 
x = -1
result_rec = BinarySearchRecursive(array, 0, len(arr)-1, x)
result_iter = BinarySearchIterative(array, 0, len(arr)-1, x)  

x3 = 0 
print('Test the first element:')
result_rec = BinarySearchRecursive(array, 0, len(arr)-1, x)
result_iter = BinarySearchIterative(array, 0, len(arr)-1, x) 

x2 = 20
print('Test the last element:')
result_rec = BinarySearchRecursive(array, 0, len(arr)-1, x)
result_iter = BinarySearchIterative(array, 0, len(arr)-1, x)  
