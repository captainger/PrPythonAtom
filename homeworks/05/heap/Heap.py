import operator
class Heap():
    
    def __init__(self, array):
        self.array = array[:]
        self.is_max_heap =  operator.gt
        self.comparator = operator.gt
    
    def __len__(self):
        return(len(self.array))

    def add(self, elem_with_priority):
        self.array.append(elem_with_priority)
        self._shift_up(len(self.array) - 1)
    
    def _shift_up(self,i): 
        parent = (i - 1) // 2
        while i > 0 and self.comparator(self.array[i], self.array[parent]):
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            i = parent
            parent = (i - 1) //2
    
    def _shift_down(self, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        heap_size = len(self.array) - 1
        if left <= heap_size and self.comparator(self.array[left], self.array[largest]):
            largest = left
        if right <= heap_size and self.comparator(self.array[right], self.array[largest]):
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self._shift_down(largest)
    
    def _build_heap(self):
        heap_size = len(self.array) - 1
        for i in range(heap_size // 2 + 1, -1, -1):
            self._shift_down(i)
        
    
    def show_tree(self, total_width=33, fill=' '):
        tree = self.array
        
        import math
        from io import StringIO
        output = StringIO()
        last_row = -1
        for i, n in enumerate(tree):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print (output.getvalue())
        print ('-' * total_width)
        print()
    
class MinHeap(Heap):
    
    def __init__(self, array):
        self.array = array[:]
        self.is_max_heap = False
        self.comparator = lambda x, y: x < y
        self._build_heap()
        
    def extract_minimum(self):
        mn = self.array[0]
        last = self.array.pop()
        if len(self.array) > 0:
            self.array[0] = last
            self._shift_down(0)
        return mn
