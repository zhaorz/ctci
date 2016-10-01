# median.py
# ~~~~~~~~~
# Numbers are randomly generated and passed to a method. Write a program to
# find and maintain the median value as new values are generated.

from ctci.lib.PriorityQueue import PriorityQueue

class MedianArray(object):

    def __init__(self):
        self.left  = PriorityQueue(lambda x, y: True if x > y else False)
        self.right = PriorityQueue(lambda x, y: True if x < y else False)
        self.median = None

    def add(self, value):
        if (len(self.right) == 0):
            self.left.add(value)
        elif (value > self.right.peek()):
            self.right.add(value)
        else:
            self.left.add(value)

        # Balance queues
        if (abs(len(self.left) - len(self.right)) > 1):
            if (len(self.left) > len(self.right)):
                longer = self.left
                shorter = self.right
            else:
                longer = self.right
                shorter = self.left

            shorter.add(longer.remove())

        return None

    def getMedian(self):
        if (len(self.left) == 0 and len(self.right) == 0):
            return None
        elif (len(self.left) == 0):
            assert(len(self.right) == 1)
            return self.right.peek()
        elif (len(self.right) == 0):
            assert(len(self.left) == 1)
            return self.left.peek()
        else:
            lo = self.left.peek()
            hi = self.right.peek()
            if (len(self.left) == len(self.right)):
                return (lo + hi) // 2
            elif (len(self.left) > len(self.right)):
                return lo
            else:
                return hi


class TestMedianArray(object):

    def __init__(self):
        print('Running MedianArray tests')
        self.testGetMedian()
        print('Done\n')

    def testGetMedian(self):
        M = MedianArray()
        M.add(1)
        assert(M.getMedian() == 1)
        M.add(2)
        assert(M.getMedian() == 1)
        M.add(7)
        assert(M.getMedian() == 2)
        M.add(6)
        assert(M.getMedian() == 4)
        M.add(17)
        assert(M.getMedian() == 6)
        print('getMedian passed')

