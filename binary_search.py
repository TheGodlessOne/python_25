class BinarySearch:
    def __init__(self, array, left, right): 
        self.arr = array 
        self.left = left 
        self.right = right 


    def search(self, x, search_type): 
        if search_type == 'rec': 
            result = self.recursive(x)
        elif search_type == 'iter': 
            result = self.iterative(x)
        
        if result is None: 
            print("There's no such element in array")
        else: 
            print("Element {0} is presented at {1} position by {2} algorithm".format(x, result, search_type))


    def recursive(self, x): 
        if self.right >= self.left: 
            middle = int(self.left + (self.right - self.left)/2)
            if self.arr[middle] == x: 
                return middle 
            elif self.arr[middle] > x: 
                self.right = middle - 1
                return self.recursive(x) 
            else: 
                self.left = middle + 1
                return self.recursive(x) 


    def iterative(self, x): 
        while self.left <= self.right: 
            middle = int(self.left + (self.right - self.left)/2) 
            if self.arr[middle] == x: 
                return middle 
            elif self.arr[middle] < x: 
                self.left = middle + 1
            else: 
                self.right = middle - 1
        return None


test_arr = [i for i in range(20)]
test_search = BinarySearch(test_arr, 0, len(test_arr))
print(test_search.search(4, 'rec'))
print(test_search.search(4, 'iter'))
