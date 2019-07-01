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

    def print(self):
        print("  node" + str(self.value) + "(" + str(self.balance) + "," + str(self.potential) + ")")

    def addEdge(self, edge):
        if self.value == edge.node.value:
            return
        self.edges[edge.node.value] = edge


class Edge:

    flow = 0

    def __init__(self, node, capacity, weight):
        self.node = node
        self.capacity = capacity
        self.weight = weight
        self.residualCapacity = capacity
        self.reductWeight = weight

    def print(self):
        print("     edge(" + str(self.node.value) + ") = (" + str(self.residualCapacity) + "," +
              str(self.weight) + "," + str(self.reductWeight) + "," + str(self.flow) + ")")