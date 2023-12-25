import networkx as nx
import matplotlib.pyplot as plt


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    G = nx.DiGraph()
    for i in lines:
        tmp = i.split(': ')
        current_point = tmp[0]
        other_points = [k for k in tmp[1].split(' ')]
        for l in other_points:
            G.add_edges_from([(current_point, l)])
            G.add_edges_from([(l, current_point)])
    return G


G = read_file('input_day25.txt')
edges_to_remove = nx.minimum_edge_cut(G)
for i in edges_to_remove:
    G.remove_edge(i[0], i[1])
    G.remove_edge(i[1], i[0])

# make an undirected copy of the digraph
UG = G.to_undirected()

components = [UG.subgraph(c).copy() for c in nx.connected_components(UG)]
result = 1
for idx, g in enumerate(components, start=1):
    # print(f"Component {idx}: Nodes: {g.nodes()} Edges: {g.edges()}")
    result *= len(g.nodes())

print(result)

#print
# Specify the edges you want here
edge_colours = ['black' for edge in G.edges()]
black_edges = [edge for edge in G.edges()]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_size=50)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()
