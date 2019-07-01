import sys
from PriorityQueue import PriorityQueue

def dijkstra(nodes,root):

    costs = []
    for i in range(len(nodes) + 1):
        costs.append((sys.maxsize, root))

    costs[root] = (0, root)
    visited = [False for i in range(len(nodes) + 1)]

    # queue contains open nodes to visit
    queue = PriorityQueue((root,0))

    # update costs while queue is not empty
    while not queue.isEmpty():

        # remove node from queue
        node = queue.pop()

        # mark node visited
        visited[node] = True

        # expand node and update path costs
        for edge in nodes[node-1].edges.values():
            if not visited[edge.node.value] \
                    and edge.reductWeight + costs[node][0] < costs[edge.node.value][0] \
                    and edge.residualCapacity > 0:
                costs[edge.node.value] = (edge.reductWeight + costs[node][0], node)

                if not queue.contains(edge.node.value):
                    queue.add((edge.node.value,costs[edge.node.value]))

   # print(costs)
    return costs

class Graph:

    def __init__(self,nodes):
        self.nodes = nodes

    def addNode(self,node):
        self.nodes.append(node)

    def print(self):
        print("nodes (balance,potential)")
        print("  edges(node1,node2)=(capacity,weight,reductWeight,flow)\n")

        cost = 0
        for node in self.nodes:
            node.print()
            for edge in node.edges.values():
                edge.print()
                cost += edge.weight * edge.flow

        print("\ntotal cost = " + str(cost))

    def findPath(self, overflowNodes, defectsNodes):

        for root in overflowNodes:
            # apply Dijkstra algorithm
            costs = dijkstra(self.nodes,root)

            for i in range(len(self.nodes)):
                if costs[i+1][0] != sys.maxsize:
                    self.nodes[i].potential -= costs[i+1][0]

            for end in defectsNodes:
                # check if end node is reachable, that is the cost of its path is != sys.maxsize
                if costs[end][0] == sys.maxsize:
                    continue

                path = [end]

                # iterative search for predecessors
                while end != root:
                    path.append(costs[end][1])
                    end = costs[end][1]

                if path:
                    path.reverse()
                    return path

        return []

    # increase flow in edges of the path
    def updateFlow(self, flow, path):
        for i in range(len(path)-1):
            edge = self.nodes[path[i]-1].edges[path[i+1]]
            edge.flow += flow
            edge.residualCapacity -= flow

    def updateCosts(self):
        for node in self.nodes:
            for edge in node.edges.values():
                if edge.residualCapacity > 0:
                    edge.reductWeight = edge.weight - node.potential + edge.node.potential

    def updateBalance(self, root, end, flow):
        self.nodes[root-1].balance -= flow
        self.nodes[end-1].balance += flow