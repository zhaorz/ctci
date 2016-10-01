# DirectedGraph.py
# ~~~~~~~~~~~~~~~~
#
#


class DirectedGraph(object):

    def __init__(self):
        self.nodes = dict()

    def addVertex(self, node):
        if node in self.nodes:
            raise Exception('cannot add a node that already exists')
        self.nodes[node] = set()
        return None

    def removeVertex(self, node):
        if node not in self.nodes:
            raise Exception('remove node that does not exist')
        del self.nodes[node]
        return None

    def addEdge(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise Exception('node not in 

    def removeEdge(self, node1, node2):
        pass

    def hasEdge(self, node1, node2):
        pass

    def neighbors(self, node):
        pass




class TestDirectedGraph(object):

    def __init__(self):
        print('Running DirectedGraph tests...')
        self.testAddVertex()
        self.testRemoveVertex()
        print('Passed')

    def testAddVertex(self):
        G = DirectedGraph()
        G.addVertex(5)
        assert(5 in G.nodes)
        print('addVertex passed')

    def testRemoveVertex(self):
        G = DirectedGraph()
        G.addVertex(42)
        assert(42 in G.nodes)
        G.removeVertex(42)
        assert(42 not in G.nodes)
        print('removeVertex passed')



