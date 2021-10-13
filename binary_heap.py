#
#   MIN HEAP
#
class Heap:

    def __init__(self):
        self.heap = []

    def __siftUp(self):
        curr = len(self.heap) - 1
        while curr > 0:
            p = (curr - 1)//2
            data = self.heap[curr]
            parent = self.heap[p]
            if data.f < parent.f:
                temp = parent
                self.heap[p] = data
                self.heap[curr] = parent
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
                temp = self.heap[j]
                self.heap[j] = self.heap[max]
                self.heap[max] = temp
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
        if item is None:
            return False

        temp = self.heap[0] 
        self.heap[0] = item #we replace the current min with the item we want to delete
        self.delete() 
        self.insert(temp)
        return True

    
    def size(self):
        return len(self.heap)

    #peek returns F value of min node
    def peek(self):
        return self.heap[0].f
    
    def print(self):
        print("[", end="")
        for cell in self.heap:
            print(cell.f, end=",")
        print("]")