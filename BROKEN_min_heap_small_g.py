import random
#
#   Min heap
#   Breaks ties with smaller g-value
#
class Heap():

    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = self.heap[i]

    def __siftUp(self):
        currIndex = len(self.heap) - 1
        while currIndex > 0:
            parentIndex = (currIndex - 1)//2
            current = self.heap[currIndex]
            parent = self.heap[parentIndex]

            if current.f == parent.f: #TIE BREAK 
                if current.g < parent.g: # CHOOSE SMALLER G VALUE
                    self.swap(parentIndex, currIndex)
                    currIndex = parentIndex

                elif current.g == parent.g: #if G values are == then we randomly choose the tie break
                    rand = random.random() 
                    if rand < 0.5:
                        self.swap(parentIndex, currIndex)
                        currIndex = parentIndex 
                else:
                    break

            elif current.f < parent.f:
                self.swap(parentIndex, currIndex)
                currIndex = parentIndex
            else:
                break
    
    def __siftDown(self):
        current_index = 0
        left_index = 2*current_index+1

        while left_index < len(self.heap):
            right_index = left_index + 1
            max_index = left_index

            left = self.heap[left_index]
            current = self.heap[current_index]

            if right_index < len(self.heap):
                right = self.heap[right_index]
                if (right.f < left.f):
                    max_index += 1
                elif (right.f == left.f): #tie break f values
                    if (right.g == left.g): #tie break eaqual g values
                        rand = random.random() 
                        if rand < 0.5:
                            max_index += 1

                    elif (right.g < left.g):
                        max_index += 1


            max = self.heap[max_index]
            if (current.f > max.f):
                self.swap(current_index, max_index)
                current_index = max_index
                left_index = 2*current_index+1

            elif current.f == max.f: #Tie break f values 
                if (current.g > max.g): #TODO: check this sign < >
                    self.swap(current_index, max_index)
                    current_index = max_index
                    left_index = 2*current_index+1

                elif current.g == max.g: #if G values are == then we randomly choose the tie break
                    rand = random.random() 
                    if rand < 0.5:
                        self.swap(current_index, max_index)
                        current_index = max_index
                        left_index = 2*current_index+1
                else:
                    break
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
            