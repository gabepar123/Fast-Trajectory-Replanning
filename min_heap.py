import random
#
#   MIN HEAP
#
class Heap:

    use_smallest_g = True
    def __init__(self, use_smallest_g):
        self.heap = []
        self.use_smallest_g = use_smallest_g


    #True = c1 > c2
    def compc(self, c1, c2):
        if (c1.f > c2.f): return True
        if (c1.f < c2.f): return False
        if (c1.f == c2.f):
            if (self.use_smallest_g):
                if (c1.g > c2.g): return True #smallest G
                #print("bool")
            else:
                if (c1.g < c2.g): return True
                #print("fo")
        rand = random.random()
        if rand > 0.5: 
            return False
        return True


    def __siftUp(self):
        curr = len(self.heap) - 1
        while curr > 0:
            p = (curr - 1)//2
            data = self.heap[curr]
            parent = self.heap[p]
            if self.compc(parent, data):
            # if 10*(data.f - data.g) < 10*(parent.f - parent.g)
            #if data.f < parent.f: #TODO:
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
                if self.compc(self.heap[k], self.heap[i]):
                #if self.heap[i].f < self.heap[k].f: #TODO:
                    max += 1
            if self.compc(self.heap[j], self.heap[max]):
            #if (self.heap[j].f > self.heap[max].f): #TODO:
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
            print([cell.f, cell.g], end=",")
        print("]")
    
   