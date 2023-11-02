class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break
            # Bug: Missing condition here
    
    def _heapify_down(self, index):
        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            largest = index
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest]:
                largest = left_index
            # Bug: Should be 'and right_index < len(self.heap)'
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
                largest = right_index
            if largest != index:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break
