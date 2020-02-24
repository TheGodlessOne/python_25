class BinarySearch:
    def __init__(self, array): 
        self.arr = array 
        self.left = self.arr[0] 
        self.right = self.arr[-1] 


    def search(self, x, search_type): 
        if search_type == 'rec': 
            while True:
                try: 
                    if (x<self.arr[0]or x>self.arr[-1]): raise IndexError
                    return self.recursive(x, self.left, self.right)
                    break
                except IndexError: 
                    print("Value {0} is too small or too big".format(x))
                    break
        elif search_type == 'iter': 
            while True:
                try: 
                    if (x<self.arr[0]or x>self.arr[-1]): raise IndexError
                    return self.iterative(x, self.left, self.right)
                    break
                except IndexError: 
                    print("Value {0} is too small or too big".format(x))
                    break


    def recursive(self, x, l, r): 
        if r >= l: 
            m = int(l + (r - l)/2)
            if self.arr[m] == x: 
                return m 
            elif self.arr[m] > x: 
                r = m - 1
                return self.recursive(x, l, r) 
            else: 
                l = m + 1
                return self.recursive(x, l, r) 
        else: 
            return None


    def iterative(self, x, l, r):
        while l <= r: 
            m = int(l + (r - l)/2) 
            if self.arr[m] == x: 
                return m
            elif self.arr[m] < x: 
                l = m + 1
            else: 
                r = m - 1
        return None


s_types = ['rec', 'iter']
test_arr = [i*2 for i in range(20)]
print(test_arr)
cases = {
        'first element': test_arr[0],
        'last element': test_arr[-1],
        'lesser than minimum': -1,
        'bigger than maximum': 100,
        'not in the list, but in range': 15
}
test_search = BinarySearch(test_arr)
for s_type in s_types:
    print('Test the {0} alg'.format(s_type))
    for test_case in cases.items(): 
        x = test_case[1]
        print("Test case: {0}; test value: {1}".format(test_case[0], x))
        if test_search.search(x, s_type) is not None: 
            print("Value {0} has index {1} by {2} algorithm".format(x, test_search.search(x, s_type), s_type))
        else: 
            print("Value {0} is out of list".format(x))
