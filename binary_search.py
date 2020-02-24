class BinarySearch:
    def __init__(self, x, array, left, right): 
        self.arr = array 
        self.left = left 
        self.right = right 
        self.x = x

    def recursive(self): 
        if self.right >= self.left: 
            middle = int(self.left + (self.right - self.left)/2)
            if self.arr[middle] == self.x: 
                return middle 
            elif self.arr[middle] > self.x: 
                self.right = middle - 1
                return self.recursive() 
            else: 
                self.left = middle + 1
                return self.recursive() 

    def iterative(self): 
        while self.left <= self.right: 
            middle = int(self.left + (self.right - self.left)/2) 
            if self.arr[middle] == self.x: 
                return middle 
            elif self.arr[middle] < self.x: 
                self.left = middle + 1
            else: 
                self.right = middle - 1
        return None


print('Test the empty array:')
test_arr = [i for i in range(20)]
test_search = BinarySearch(4, test_arr, 0, len(test_arr))
print(test_search.recursive())
print(test_search.iterative())

# arr = [i for i in range(20)]
# print('Test the non-existing element:')
# x = 40

# x = -1


# x3 = 0 
# print('Test the first element:')


# x2 = 20
# print('Test the last element:')
  
