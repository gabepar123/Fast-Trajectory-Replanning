#
#   MIN HEAP
#
class Heap:

    heap = []

    def __siftUp(self):
        curr = len(self.heap) - 1
        while curr > 0:
            p = (curr - 1)//2
            data = self.heap[curr]
            parent = self.heap[p]
            if data < parent:
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
                if self.heap[i] < self.heap[k]:
                    max += 1
            if (self.heap[j] > self.heap[max]):
                temp = self.heap[j]
                self.heap[j] = self.heap[max]
                self.heap[max] = temp
                j = max
                k = 2 * j + 1
            else:
                break
    
    def size(self):
        return len(self.heap)
    
    def print(self):
        print(self.heap)