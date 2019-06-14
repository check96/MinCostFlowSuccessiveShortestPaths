class Node:

    potential = 0

    def __init__(self,value,balance,edges):
        self.value = value
        self.balance = balance
        self.edges = edges

    def setBalance(self,balance):
        self.balance = balance

    def setPotential(self,potential):
        self.potential = potential

    def addFlow(self,flow,edge):
        for e in self.edges:
            if e.node.value == edge:
                e.flow += flow
                e.capacity -= flow

    def print(self):
        print("  node" + str(self.value) + "(" + str(self.balance) + "," + str(self.potential) + ")")

    def addEdge(self, edge):
        self.edges.append(edge)

    def getCapacity(self, edge):
        for e in self.edges:
            if e.node.value == edge:
                return e.capacity

class Edge:

    flow = 0

    def __init__(self, node, capacity, weight):
        self.node = node
        self.capacity = capacity
        self.weight = weight

    def print(self):
        print("     edge(" + str(self.node.value) + ") = (" + str(self.capacity) + "," +
              str(self.weight) + "," + str(self.flow) + ")")