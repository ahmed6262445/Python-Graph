import breadth_first_search
import depth_first_search
from adjacency_matrix_graph import AdjacencyMatrixGraph

g = AdjacencyMatrixGraph(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

depth_first_search.depth_first(g,1)
breadth_first_search.breadth_first(g,1)