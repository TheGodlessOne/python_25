class BinarySearch:
    def __init__(self, array, left, right): 
        self.arr = array 
        self.left = left 
        self.right = right 


    def is_inbound(self): 
        if x<self.arr[0]: 
            raise IndexError
        if x>self.arr[-1]: 
            raise IndexError


    def search(self, x, search_type): 
        if search_type == 'rec': 
            try: 
                return self.recursive(x)
            except IndexError: 
                print("Value {0} is too small or too big".format(x))
        elif search_type == 'iter': 
            try: 
                return self.iterative(x)
            except IndexError: 
                print("Value {0} is too small or too big".format(x))


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


s_types = ['rec', 'iter']
test_arr = [i for i in range(20)]
print(test_arr)
print(test_arr[-1])
cases = [test_arr[0], test_arr[int(len(test_arr)/2)], test_arr[-1], -1, 100]
test_search = BinarySearch(test_arr, 0, len(test_arr))
for x in cases: 
    print(x)
    for s_type in s_types:
        if test_search.search(x, s_type) is None: 
            print(test_search.search(x, s_type))
        else: 
            print("Value {0} has index {1} by {2} algorithm".format(x, test_search.search(x, s_type), s_type))
