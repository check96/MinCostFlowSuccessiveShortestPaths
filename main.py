import sys
import networkx as nx
import matplotlib.pyplot as plt
from string import ascii_lowercase

from Graph import Graph
from Elements import Node
from Elements import Edge

def drawGraph(graph, node_size=1500, node_color='blue', node_alpha=0.3,
               node_text_size=12,  edge_alpha=0.8, edge_tickness=1, edge_text_pos=0.7,  text_font='sans-serif', ):
    G = nx.DiGraph()
    C = nx.Graph()

    edges = []

    cost = 0
    for node in graph.nodes:
        G.add_node(node.value)
        for edge in node.edges.values():
            G.add_edge(node.value, edge.node.value)
            edges.append((node.value, edge.node.value, edge.weight, edge.flow))
            cost += edge.weight * edge.flow

    C.add_node(cost)
    # draw graph
    # layout: spring, shell, random, spectral
    graph_pos = nx.shell_layout(G)

    nx.draw_networkx_nodes(G, graph_pos, node_size=node_size, alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G, graph_pos, width=edge_tickness, alpha=edge_alpha, edge_color='green',
                           node_size=node_size, connectionstyle='arc3,rad=-0.15')

    node_labels = {}
    for idx, node in enumerate(G.nodes()):
        node_labels[node] = ascii_lowercase[idx]
    nx.draw_networkx_labels(G, graph_pos, label=node_labels, font_size=node_text_size, font_family=text_font)

    labels = [(edge[2], edge[3]) for edge in edges]
    _edges = [(edge[0], edge[1]) for edge in edges]
    edge_labels = dict(zip(_edges, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, label_pos=edge_text_pos)

    # draw cost
    c_pos = nx.shell_layout(C)
    for idx, node in enumerate(C.nodes()):
        node_labels[node] = ascii_lowercase[idx]
    nx.draw_networkx_nodes(C, c_pos, node_size=node_size, alpha=node_alpha, node_color='red')
    nx.draw_networkx_labels(C, c_pos, label=node_labels, font_size=node_text_size, font_family=text_font)

    # save figure
    plt.savefig("path.png")
    plt.close()


def drawResidualGraph(graph, iteration, node_size=1500, node_color='blue', node_alpha=0.3,
               node_text_size=12,  edge_alpha=0.8, edge_tickness=1, edge_text_pos=0.75,  text_font='sans-serif', ):

    G = nx.DiGraph()

    edges = []
    backEdges = []

    for node in graph.nodes:
        G.add_node(node.value)

        for edge in node.edges.values():
            if edge.residualCapacity > 0:
                G.add_edge(node.value, edge.node.value)
                edges.append((node.value, edge.node.value, edge.reductWeight, edge.residualCapacity))
            if edge.flow > 0:
                G.add_edge(edge.node.value, node.value)
                backEdges.append((edge.node.value, node.value, edge.reductWeight, edge.flow))

  #
    # draw graph
    graph_pos = nx.shell_layout(G)

    # draw node
    nx.draw_networkx_nodes(G, graph_pos, node_size=node_size, alpha=node_alpha, node_color=node_color)

    # draw edges
    nx.draw_networkx_edges(G, graph_pos, width=edge_tickness, alpha=edge_alpha, edge_color='green',
                           node_size = node_size, connectionstyle='arc3,rad=0.15')

    # draw node labels

    nx.draw_networkx_labels(G, graph_pos, font_size=node_text_size, font_family=text_font)

    labels = [(edge[2],edge[3]) for edge in edges]
    forwardEdges = [(edge[0],edge[1]) for edge in edges]
    edge_labels = dict(zip(forwardEdges, labels))

    # draw forward edges labels
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, label_pos=edge_text_pos, font_size=7)

    backLabels = [(edge[2], edge[3]) for edge in backEdges]
    backwardEdges = [(edge[0], edge[1]) for edge in backEdges]
    back_edge_labels = dict(zip(backwardEdges, backLabels))

    # draw backward edges labels
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=back_edge_labels, label_pos=edge_text_pos, font_size=7)

    plt.savefig("path" + str(iteration) + ".png")
    plt.close()
    # show graph
    #plt.show()


# node(value,balance, { exitEdges(node,capacity,weight})

node6 = Node(6,-2, {})
node5 = Node(5,0, {6: Edge(node6,2,2)})
node4 = Node(4,-2, {5: Edge(node5,1,2), 6: Edge(node6,1,2)})
node2 = Node(2,0, {4: Edge(node4,6,5)})
node3 = Node(3,1, {2: Edge(node2,2,1), 4: Edge(node4,5,2), 5: Edge(node5,2,2)})
node1 = Node(1,3, {2: Edge(node2,4,2), 3: Edge(node3,1,3)})
nodes = [node1,node2,node3,node4,node5,node6]

'''
node6 = Node(6,-5, {})
node5 = Node(5,-2, {6: Edge(node6,9,3)})
node2 = Node(2,0, {5: Edge(node5,5,1)})
node3 = Node(3,0, {2: Edge(node2,5,4), 6: Edge(node6,5,2)})
node4 = Node(4,0, {6: Edge(node6,7,2), 3: Edge(node3,2,5)})
node1 = Node(1,7, {2: Edge(node2,6,2), 3: Edge(node3,7,3), 4: Edge(node4,5,1)})
nodes = [node1,node2,node3,node4,node5,node6]
'''
'''
node4 = Node(4,-4, {})
node3 = Node(3,0, {4: Edge(node4,5,1)})
node2 = Node(2,0, {3: Edge(node3,2,1), 4: Edge(node4,3,3)})
node1 = Node(1,4, {2: Edge(node2,4,2), 3: Edge(node3,2,2)})
nodes = [node1,node2,node3,node4]
'''
defectsNode = []
overflowNode = []

graph = Graph(nodes)

# create overflowNodes and defectNodes list
for node in graph.nodes:
    if node.balance > 0:
        overflowNode.append(node.value)
    elif node.balance < 0:
        defectsNode.append(node.value)

print("overflow = " + str(overflowNode))
print("defect = " + str(defectsNode)+ "\n")
iteration = 0
drawResidualGraph(graph,iteration)
iteration += 1

while len(overflowNode) > 0 and len(defectsNode) > 0:
    path = graph.findPath(overflowNode, defectsNode)
  #  print(path)

    # check if there is no path from overflowNodes to defectNodes
    if path == []:
        break

    # find minimum residual capacity in path
    minim = sys.maxsize
    for i in range(len(path)-1):
        residual = graph.nodes[path[i] - 1].edges[path[i+1]].residualCapacity
        if residual < minim:
            minim = residual

    # find minimum flow that can be sent in the path
    flow = min(abs(graph.nodes[path[0]-1].balance), abs(graph.nodes[path[-1]-1].balance), minim)
    #print(flow)

    # increase flow and update reduct costs in edges of the path
    graph.updateCosts()
    graph.updateFlow(flow, path)

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

    drawResidualGraph(graph,iteration)
    iteration += 1
    graph.print()

drawGraph(graph)