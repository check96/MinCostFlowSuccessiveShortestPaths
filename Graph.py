import sys


def dijkstra(nodes,root):

    costs = []
    for i in range(len(nodes) + 1):
        costs.append((sys.maxsize, root))

    costs[root] = (0, root)
    visited = [False for i in range(len(nodes) + 1)]

    # queue contains open nodes to visit
    queue = [root]

    # update costs while queue is not empty
    while queue != []:

        # select node with minimum path cost to expand
        min = sys.maxsize
        node = 0
        for v in queue:
            if costs[v][0] < min:
                min = costs[v][0]
                node = v

        # remove node from queue
        queue.remove(node)

        # mark node visited
        visited[node] = True

        # expand node and update path costs
        for edge in nodes[node-1].edges:
            if not visited[edge.node.value] and edge.reductWeight + costs[node][0] < costs[edge.node.value][0] \
                    and edge.residualCapacity > 0:
                costs[edge.node.value] = (edge.reductWeight + costs[node][0], node)

                if edge.node.value not in queue:
                    queue.append(edge.node.value)

   # print(costs)
    return costs

class Graph:

    def __init__(self,nodes):
        self.nodes = nodes

    def addNode(self,node):
        self.nodes.append(node)

    def print(self):
        print("nodes (balance,potential)")
        print("  edges(node1,node2)=(capacity,weight,flow)\n")
        for node in self.nodes:
            node.print()
            for edge in node.edges:
                edge.print()


    def findPath(self, root, end):
        '''
            apply Dijkstra algorithm and return minimum shortest path from root to end
        '''

        costs = dijkstra(self.nodes,root)

        for i in range(len(self.nodes)):
            self.nodes[i].potential = costs[i+1][0]

        path = [end]
        # iterative search for predecessors
        while end != root:
            path.append(costs[end][1])
            end = costs[end][1]

        path.reverse()
        return path

    # increase flow in edges of the path
    def updateFlow(self, flow, path):
        for i in range(len(path)-1):
            self.nodes[path[i]-1].updateFlow(flow,path[i+1])

    def updateCosts(self, path):
        for i in range(len(path) - 1):
            self.nodes[i].updateCost(path[i+1])

    def updateBalance(self, root, end, flow):
        self.nodes[root-1].balance += flow
        self.nodes[end-1].balance -= flow
