class KthLargest:
    heap = None
    k = None
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.makeHeap(nums, k)

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            if val > self.heap[0]:
                self.heap[0] = val
                self.downHeapify(0)
        else:
            self.heap.append(val)
            self.downHeapify(0)
        return self.heap[0]
    
    def makeHeap(self, nums, k):
        self.heap = nums[:k]
        self.downHeapify(0)
        
        for i in range(k, len(nums)):
            self.add(nums[i])
        
    def downHeapify(self, index):
        leftChild = 2 * index + 1
        rightChild = 2 * index + 2
        
        if leftChild < len(self.heap) and self.heap[leftChild] < self.heap[index]:
            self.swap(leftChild, index)
            self.downHeapify(leftChild)
            self.upHeapify(index)
        
        if rightChild < len(self.heap) and self.heap[rightChild] < self.heap[index]:
            self.swap(rightChild, index)
            self.downHeapify(rightChild)
            self.upHeapify(index)
                
    def upHeapify(self, child):
        parent = child // 2
        if parent != child and self.heap[parent] > self.heap[child]:
            self.swap(parent, child)
            self.upHeapify(parent)
            self.downHeapify(child)
        
    def swap(self, index1, index2):
        val1 = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = val1
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
