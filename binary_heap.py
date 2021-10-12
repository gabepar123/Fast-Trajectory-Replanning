#
#   MIN HEAP
#
class Heap:

    heap = []

    def __siftUp(self):
        curr = len(self.heap) - 1
        while curr > 0:
            p = (curr - 1)//2
            data = self.heap[curr].f
            parent = self.heap[p].f
            if data < parent:
                temp = parent
                self.heap[p].f = data
                self.heap[curr].f = parent
                curr = p
            else:
                break
    
    def insert(self, x):
        self.heap.append(x)
        self.__siftUp()

    # Returns Min item
    def delete(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is Empty")

        if len(self.heap) == 1:
            return self.heap.pop(0)
        
        data = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap) - 1)
        self.__siftDown()
        return data
    
    def __siftDown(self):
        j = 0
        k = 2 * j + 1
        while k < len(self.heap):
            max = k
            i = k + 1
            if i < len(self.heap):
                if self.heap[i].f < self.heap[k].f:
                    max += 1
            if (self.heap[j].f > self.heap[max].f):
                temp = self.heap[j].f
                self.heap[j].f = self.heap[max].f
                self.heap[max].f = temp
                j = max
                k = 2 * j + 1
            else:
                break
    #LAZY heap delete
    def deleteItem(self, x):
        #search for item
        item = None
        for cell in self.heap:
            if cell == x:
                item = cell
        if item == None:
            return False

        temp = self.heap[0] 
        self.heap[0] = item #we replace the current min with the item we want to delete
        self.delete() 
        self.insert(temp)
        return True

    
    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0].f
    
    def print(self):
        print(self.heap)