import sys

from Graph import Graph
from Elements import Node
from Elements import Edge


node6 = Node(6,2, {})
node5 = Node(5,0, {6: Edge(node6,2,2)})
node4 = Node(4,2, {5: Edge(node5,1,2), 6: Edge(node6,1,2)})
node2 = Node(2,0, {4: Edge(node4,6,5)})
node3 = Node(3,-1, {2: Edge(node2,2,1), 4: Edge(node4,5,2), 5: Edge(node5,2,2)})
node1 = Node(1,-3, {2: Edge(node2,4,2), 3: Edge(node3,1,3)})

nodes = [node1,node2,node3,node4,node5,node6]

defectsNode = []
overflowNode = []

graph = Graph(nodes)

# create overflowNodes and defectNodes list
for node in graph.nodes:
    if node.balance < 0:
        overflowNode.append(node.value)
    elif node.balance > 0:
        defectsNode.append(node.value)

while len(overflowNode) > 0 and len(defectsNode) > 0:
    path = graph.findPath(overflowNode, defectsNode)
  #  print(path)

    # check if there is no path from overflowNodes to defectNodes
    if path is []:
        break

    # find minimum residual capacity in path
    minim = sys.maxsize
    for i in range(len(path)-1):
        residual = graph.nodes[path[i] - 1].edges[path[i+1]].residualCapacity
        if residual < minim:
            minim = residual

    # find minimum flow that can be sent in the path
    flow = min(abs(graph.nodes[path[0]-1].balance), graph.nodes[path[-1]-1].balance, minim)
    #print(flow)

    # increase flow and update reduct costs in edges of the path
    graph.update(flow, path)

    # update balances of root and end node in path
    graph.updateBalance(path[0], path[-1], flow)

    # check if root node can exit from overflowNode
    if graph.nodes[path[0]-1].balance == 0:
        overflowNode.remove(path[0])

    # check if end node can exit from defectNode
    if graph.nodes[path[-1]-1].balance == 0:
        defectsNode.remove(path[-1])

    #print(overflowNode)
    #print(defectsNode)

graph.print()

