class Node:

    potential = 0

    def __init__(self,value,balance,edges):
        self.value = value
        self.originalBalance = balance
        self.balance = balance
        self.edges = edges

    def setBalance(self,balance):
        self.balance = balance

    def setPotential(self,potential):
        self.potential = potential

    def updateFlow(self,flow,edge):
        for e in self.edges:
            if e.node.value == edge:
                e.flow += flow
                e.residualCapacity -= flow

    def updateCost(self,edge):
        for e in self.edges:
            if e.node.value == edge:
                e.reductWeight = e.reductWeight + self.potential - e.node.potential


    def print(self):
        print("  node" + str(self.value) + "(" + str(self.originalBalance) + "," + str(self.potential) + ")")

    def addEdge(self, edge):
        self.edges.append(edge)

    def getResidual(self, edge):
        for e in self.edges:
            if e.node.value == edge:
                return e.residualCapacity


class Edge:

    flow = 0

    def __init__(self, node, capacity, weight):
        self.node = node
        self.capacity = capacity
        self.weight = weight
        self.residualCapacity = capacity
        self.reductWeight = weight

    def print(self):
        print("     edge(" + str(self.node.value) + ") = (" + str(self.capacity) + "," +
              str(self.weight) + "," + str(self.flow) + ")")