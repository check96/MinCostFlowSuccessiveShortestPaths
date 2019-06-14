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

graph = Graph(nodes)

path = graph.findPath(node1.value,node6.value)
print(path)

graph.addFlow(5,path)
graph.print()

