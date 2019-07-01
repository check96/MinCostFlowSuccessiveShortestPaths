import networkx as nx
import matplotlib.pyplot as plt
from string import ascii_lowercase

def drawGraph(graph, node_size=1500, node_color='orange', node_alpha=0.3,
               node_text_size=12,  edge_alpha=0.8, edge_tickness=1, edge_text_pos=0.7,  text_font='sans-serif', ):
    G = nx.DiGraph()
    C = nx.Graph()

    edges = []

    cost = 0
    for node in graph.nodes:
        G.add_node(node.value)
        for edge in node.edges.values():
            if edge.flow > 0:
                G.add_edge(node.value, edge.node.value)
                edges.append((node.value, edge.node.value, edge.weight, edge.flow))
                cost += edge.weight * edge.flow

    C.add_node(cost)
    # draw graph
    # layout: spring, shell, random, spectral
    graph_pos = nx.shell_layout(G)

    nx.draw_networkx_nodes(G, graph_pos, node_size=node_size, alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G, graph_pos, width=edge_tickness, alpha=edge_alpha, edge_color='grey',
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


def drawResidualGraph(graph, iteration, node_size=1500, node_color='blue', node_alpha=0.3, node_text_size=12,
                      edge_alpha=0.8, edge_tickness=1, edge_text_pos=0.75,  text_font='sans-serif'):

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
