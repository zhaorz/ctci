# Priority Queue
# ~~~~~~~~~~~~~~
# An heap-based implementation of priority queues. The heap is represented
# as a dynamically sized array.
#
# Usage:
#   # Creates a min-heap
#   >>> PQ = PriorityQueue(lambda x, y: True if x < y else False)
#   >>> PQ.add(42)
#   >>> PQ.add(17)
#   >>> PQ.peek()
#   17
#   >>> PQ.remove()
#   17
#   >>> PQ.peek()
#   42
#

class PriorityQueue(object):
    '''Queue implementation that is highest-priority-first-out.

    PriorityQueue(higherPriority)
    Args:
        higherPriority [function] : A priority function such that
            higherPriority(x, y) == True iff x has strictly higher priority
            than y, and False otherwise.

    Interface:
        len()
            Returns the size [int] of the queue
            O(1)
        add(value)
            value [elem] : elements of the same type that higherPriority
                           acts on.
            O(log n)
        remove()
            Requires: non-empty queue
            Returns [elem] : the element removed from the queue.
            O(log n)
        peek()
            Returns [elem] : the highest priority element in the queue.
            O(1)
    '''

    def __init__(self, higherPriority):
        self.higherPriority = higherPriority
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def isEmpty(self):
        '''Returns True if the queue is empty.
        Returns:
            [bool]
        '''
        return self.heap == []

    def isNode(self, node):
        '''Returns True if node is valid with respect to the heap.
        Args:
            node [int] : The node to be checked
        Returns:
            [bool]
        '''
        return node >= 0 and node < len(self.heap)

    def swap(self, node1, node2):
        '''Swaps the values at node1 and node2 in the heap.
        Requires isNode(node1) == True, isNode(node2) == True.
        Args:
            node1 [int]
            node2 [int]
        Returns:
            [None]
        '''
        if (not(self.isNode(node1)) or not(self.isNode(node2))):
            raise Exception("Index out of range.")
        temp = self.heap[node1]
        self.heap[node1] = self.heap[node2]
        self.heap[node2] = temp
        return None

    def left(self, node):
        '''Returns the left child of node, if it exists, and None otherwise.
        Args:
            node [int]
        Returns:
            [int] The left child
            [None] If no left child exists
        '''
        child = node * 2 + 1
        if (self.isNode(child)):
            return child
        return None

    def right(self, node):
        '''Returns the right child of node, if it exists, and None otherwise.
        Args:
            node [int]
        Returns:
            [int] The right child
            [None] If no right child exists
        '''
        child = node * 2 + 2
        if (self.isNode(child)):
            return child
        return None

    def parent(self, node):
        '''Returns the parent of node, if it exists, and None otherwise.
        Args:
            node [int]
        Returns:
            [int] The parent node
            [None] If no parent node exists
        '''
        if (node == 0):
            return None
        return (node - 1) // 2

    def siftUp(self):
        '''Restores the ordering invariant by sifting the rightmost element up.
        Requires that self.heap is non-empty.
        Returns:
            [None]
        '''
        node = len(self.heap) - 1
        parent = self.parent(node)
        while (parent != None and
                self.higherPriority(self.heap[node], self.heap[parent])):
            self.swap(node, parent)
            node = parent
            parent = self.parent(node)
        return None

    def siftDown(self):
        '''Restores the ordering invariant by sifting the root element down.
        Requires that self.heap is non-empty.
        Returns:
            [None]
        '''
        # The root node is at index 0
        node = 0
        left = self.left(node)
        right = self.right(node)
        while (left != None or right != None):
            # Note that left cannot be None b/c of shape invariant
            if (right == None):
                if (self.higherPriority(self.heap[left], self.heap[node])):
                    self.swap(left, node)
                    node = left
                    left = self.left(node)
                    right = self.right(node)
                else:
                    break
            else:
                if (self.higherPriority(self.heap[left], self.heap[right])):
                    higherChild = left
                else:
                    higherChild = right
                if (self.higherPriority(
                    self.heap[higherChild], self.heap[node])):
                    self.swap(higherChild, node)
                    node = higherChild
                    left = self.left(node)
                    right = self.right(node)
                else:
                    break
        return None

    def add(self, value):
        '''Adds value to the priority queue.
        Args:
            value [int]
        Returns:
            [None]
        '''
        self.heap.append(value)
        self.siftUp()
        return None

    def remove(self):
        '''Removes the highest priority element from the queue.
        Returns:
            [int] : the element removed
        '''
        if (self.isEmpty()):
            raise Exception("remove from empty PriorityQueue")
        # Preserve shape invariant by swapping first with last
        first = 0
        last = len(self.heap) - 1
        self.swap(first, last)

        # Pop off the element to be removed and restore ordering invariant
        element = self.heap.pop()
        self.siftDown()

        return element

    def peek(self):
        '''Returns the highest priority element in the queue.
        Returns:
            [int] : the highest priority element
        '''
        if (self.isEmpty()):
            raise Exception('peek from empty PriorityQueue')
        return self.heap[0]



class TestPriorityQueue(object):

    def __init__(self):
        print("Running PriorityQueue tests")
        self.minFn = lambda x, y: True if x <= y else False
        self.testSwap()
        self.testLeft()
        self.testRight()
        self.testParent()
        self.testSiftUp()
        self.testAdd()
        self.testSiftDown()
        self.testRemove()
        self.testPeek()
        self.testLen()

    def testSwap(self):
        PQ = PriorityQueue(self.minFn)
        PQ.heap.append(1)
        PQ.heap.append(2)
        PQ.swap(0, 1)
        assert(PQ.heap == [2,1])
        try:
            PQ.swap(0,2)
        except:
            pass
        print("swap passed")

    def testLeft(self):
        PQ = PriorityQueue(self.minFn)
        PQ.heap = [1,3,2,6,7,4]
        assert(PQ.left(0) == 1)
        assert(PQ.left(1) == 3)
        assert(PQ.left(2) == 5)
        assert(PQ.left(3) == None)
        print("left passed")

    def testRight(self):
        PQ = PriorityQueue(self.minFn)
        PQ.heap = [1,3,2,6,7,4]
        assert(PQ.right(0) == 2)
        assert(PQ.right(1) == 4)
        assert(PQ.right(2) == None)
        assert(PQ.right(3) == None)
        print("right passed")

    def testParent(self):
        PQ = PriorityQueue(self.minFn)
        PQ.heap = [1,3,2,6,7,4]
        assert(PQ.parent(0) == None)
        assert(PQ.parent(1) == 0)
        assert(PQ.parent(2) == 0)
        assert(PQ.parent(3) == 1)
        assert(PQ.parent(4) == 1)
        assert(PQ.parent(5) == 2)
        print("parent passed")

    def testSiftUp(self):
        PQ = PriorityQueue(self.minFn)
        PQ.heap = [3,5,6,8,7,11,10,12,11,9,9,15]
        PQ.heap.append(9)
        PQ.siftUp()
        assert(PQ.heap == [3,5,6,8,7,9,10,12,11,9,9,15,11])
        PQ.heap = [3,5,6,8,7,11,10,12,11,9,9,15]
        PQ.heap.append(5)
        PQ.siftUp()
        assert(PQ.heap == [3,5,5,8,7,6,10,12,11,9,9,15,11])
        PQ.heap = [3,5,6,8,7,11,10,12,11,9,9,15]
        PQ.heap.append(2)
        PQ.siftUp()
        assert(PQ.heap == [2,5,3,8,7,6,10,12,11,9,9,15,11])
        PQ.heap = [1]
        PQ.siftUp()
        assert(PQ.heap == [1])
        print("siftUp passed")

    def testAdd(self):
        PQ = PriorityQueue(self.minFn)
        PQ.add(10)
        assert(PQ.heap == [10])
        PQ.add(11)
        assert(PQ.heap == [10,11])
        PQ.add(5)
        assert(PQ.heap == [5,11,10])
        PQ.add(15)
        assert(PQ.heap == [5,11,10,15])
        PQ.add(7)
        assert(PQ.heap == [5,7,10,15,11])
        PQ.add(3)
        assert(PQ.heap == [3,7,5,15,11,10])
        print("add passed")

    def testSiftDown(self):
        PQ = PriorityQueue(self.minFn)
        PQ.heap = [6,5,6,8,7,11,10,12,11,9,9,15]
        PQ.siftDown()
        assert(PQ.heap == [5,6,6,8,7,11,10,12,11,9,9,15])
        PQ.heap = [8,5,6,8,7,11,10,12,11,9,9,15]
        PQ.siftDown()
        assert(PQ.heap == [5,7,6,8,8,11,10,12,11,9,9,15])
        PQ.heap = [10,5,6,8,7,11,10,12,11,9,9,15]
        PQ.siftDown()
        assert(PQ.heap == [5,7,6,8,9,11,10,12,11,10,9,15])
        print("siftDown passed")

    def testRemove(self):
        PQ = PriorityQueue(self.minFn)
        PQ.heap = [3,7,5,15,11,10]
        assert(PQ.remove() == 3)
        assert(PQ.heap == [5,7,10,15,11])
        assert(PQ.remove() == 5)
        assert(PQ.heap == [7,11,10,15])
        assert(PQ.remove() == 7)
        assert(PQ.heap == [10,11,15])
        assert(PQ.remove() == 10)
        assert(PQ.heap == [11,15])
        assert(PQ.remove() == 11)
        assert(PQ.heap == [15])
        assert(PQ.remove() == 15)
        assert(PQ.heap == [])
        print("remove passed")

    def testPeek(self):
        PQ = PriorityQueue(self.minFn)
        PQ.add(7)
        PQ.add(2)
        PQ.add(4)
        PQ.add(10)
        PQ.add(11)
        PQ.add(3)
        assert(PQ.peek() == 2)
        assert(PQ.peek() == 2)
        assert(PQ.remove() == 2)
        assert(PQ.peek() == 3)
        print('peek passed')

    def testLen(self):
        PQ = PriorityQueue(self.minFn)
        PQ.add(7)
        PQ.add(2)
        PQ.add(4)
        PQ.add(10)
        PQ.add(11)
        PQ.add(3)
        assert(len(PQ) == 6)
        print('len passed')


if (__name__ == '__main__'):
    TestPriorityQueue()

