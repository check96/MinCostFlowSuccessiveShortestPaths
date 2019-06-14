import sys

from Graph import Graph
from Elements import Node
from Elements import Edge


node6 = Node(6,2, [])
node5 = Node(5,0, [Edge(node6,2,2)])
node4 = Node(4,2, [Edge(node5,1,2), Edge(node6,1,2)])
node2 = Node(2,0, [Edge(node4,6,5)])
node3 = Node(3,-1, [Edge(node2,2,1),Edge(node4,5,2),Edge(node5,2,2)])
node1 = Node(1,-3, [Edge(node2,4,2), Edge(node3,1,3)])

nodes = [node1,node2,node3,node4,node5,node6]

defectsNode = []
overflowNode = []

graph = Graph(nodes)

for node in graph.nodes:
    if node.balance < 0:
        overflowNode.append(node.value)
    elif node.balance > 0:
        defectsNode.append(node.value)

while len(overflowNode) > 0 and len(defectsNode) > 0:
    path = graph.findPath(overflowNode[0], defectsNode[0])
    print(path)

    if path is []:
        break

    minim = sys.maxsize
    for i in range(len(path)-1):
        if graph.nodes[path[i]-1].getCapacity(path[i+1]) < minim:
            minim = graph.nodes[path[i]-1].getCapacity(path[i+1])

    flow = min(abs(graph.nodes[overflowNode[0]-1].balance), graph.nodes[defectsNode[0]-1].balance, minim)
    print(flow)
    graph.updateFlow(flow, path)
    graph.updateCosts(path)

    graph.updateBalance(overflowNode[0], defectsNode[0], flow)

    if graph.nodes[overflowNode[0]-1].balance == 0:
        overflowNode.pop(0)

    if graph.nodes[defectsNode[0]-1].balance == 0:
        defectsNode.pop(0)

    print(overflowNode)
    print(defectsNode)
    graph.print()

