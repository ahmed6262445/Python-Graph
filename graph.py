import abc

class Graph(abc.ABC):

	def __init__(self, num_vertices, directed=False):
		"""
		Parameters:
			num_vertices (int)
		sets value for num_vertices and directed
		"""
		self.num_vertices = num_vertices
		self.directed = directed

	@abc.abstractmethod
	def add_edge(self, v1, v2, weight):
		"""
		connects two vertices and assigns weight to them
		"""
		pass

	@abc.abstractmethod
	def get_adjacent_vertices(self, v):
		"""
		returns list of neigboring vertices
		"""
		pass	

	@abc.abstractmethod
	def get_indegree(self, v):
		"""
		returns list of indegree vertices
		"""
		pass	

	@abc.abstractmethod
	def get_edge_weight(self, v1, v2):
		"""
		returns wieght of edges between two vertices
		"""
		pass

	@abc.abstractmethod
	def display(self):	
		"""
		prints the whole graph
		"""
		pass
