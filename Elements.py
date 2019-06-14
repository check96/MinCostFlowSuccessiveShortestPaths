class Node:

    potential = 0
    backwardEdges = []

    def __init__(self,value,balance,forwardEdges):
        self.value = value
        self.balance = balance
        self.forwardEdges = forwardEdges

    def setBalance(self,balance):
        self.balance = balance

    def setPotential(self,potential):
        self.potential = potential

    def addFlow(self,flow,edge):
        for e in self.forwardEdges:
            if e.node.value == edge:
                e.addFlow(flow)

    def print(self):
        print("  node" + str(self.value) + "(" + str(self.balance) + "," + str(self.potential) + ")")


class Edge:
    flow = 0

    def __init__(self, node, capacity, weight):
        self.node = node
        self.capacity = capacity
        self.weight = weight

    def addFlow(self, flow):
        self.flow += flow

    def removeFlow(self, flow):
        self.flow -= flow

    def print(self):
        print("     edge(" + str(self.node.value) + ") = (" + str(self.capacity) + "," +
              str(self.weight) + "," + str(self.flow) + ")")