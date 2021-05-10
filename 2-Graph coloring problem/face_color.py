import networkx as nx

G = nx.Graph()

colors = {0:"red", 1:"green", 2:"blue", 3:"yellow"}

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (1,3), (2,4), (3,4), (4,5)])

nodes = list(G.nodes)
edges = list(G.edges)
some_colors = ['red','green','blue','yellow']

no_of_faces = len(edges)+2-len(nodes)-1
def regionColour(regions):
    print("NO OF FACES : "+str(regions))
    for i in range(1,regions+1):
        print(f"FACE {i} : "+some_colors[i%4])

regionColour(4)