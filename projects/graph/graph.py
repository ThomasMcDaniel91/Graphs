"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # creates a vertex with an empty list as their neighboring vertices
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # add the 2nd node to the list of edges for the first node
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queueueueueueueueueue class
        to_visit = Queue()
        # create an empty set
        visited = set()
        # populating the queueueueueueue with our starting vertex
        to_visit.enqueue(starting_vertex)

        # while loop to run while the queueueueueue is not empty
        while to_visit.size() > 0:
            v = to_visit.dequeue()
            # checking to see if the dequeueueued vertex is in our set or not
            if v not in visited:
                # if it is then it gets printed out
                print(v)
                # it then gets added to the visited set
                visited.add(v)
                # now we are checking the neighbors of the vertex and adding them
                # to the queueueueueueue
                for n in self.vertices[v]:
                    to_visit.enqueue(n)

        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # create an empty stack class and set
        to_visit = Stack()
        visited = set()
        # add the starting vertex to the stack
        to_visit.push(starting_vertex)
        # while loop to run while we still have elements in our stack
        while to_visit.size() > 0:
            # pops the last value in our stack
            v = to_visit.pop()
            # checks to see if the value has already been seen
            if v not in visited:
                # if not then it gets printed out
                print(v)
                # then added to the visited set
                visited.add(v)
                # adding the neighbors to the stack class 
                for n in self.vertices[v]:
                    to_visit.push(n)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        # creating a function inside that includes a list
        # of previously traversed vertices
        def recursive(graph, traversed, vertex):
            # if the vertex is in traversed already, return none
            if vertex in traversed:
                return 
            # otherwise we print it out
            print(vertex)
            # append the vertex to our traversed list
            traversed.add(vertex)
            # running the function on the neighbors of the vertex
            for val in graph[vertex]:
                recursive(graph, traversed, val)

        recursive(self.vertices, set(), starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # creating an empty list of visited vertices
        visited = []
        # creating a queue with the starting vertex in it
        queue = [[starting_vertex]]
        # while we have items in our queueueue
        while queue:
            # pop the first item in the queueueue
            path = queue.pop(0)
            # getting the last value in our path
            node = path[-1]
            # checking to see if it has been seen already or not
            if node not in visited:
                # checking the neighbors of our farthest node
                for n in self.vertices[node]:
                    # creating a new path list and appending the nieghbors
                    # to it and the queueueueue
                    new_path = list(path)
                    new_path.append(n)
                    queue.append(new_path)
                    # if the destination is in the new_path
                    # we are done and return the new path
                    if n == destination_vertex:
                        return new_path
                # adding the node to the visited list
                visited.append(node)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print()

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print()
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
