import heapq


def calculate_distances(graph, starting_vertex):
    
    # initialize all distance as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    
    # setting starting node distance as 0
    distances[starting_vertex] = 0

    
    
    # heap that is going to proesss ie- vertex adjacent to starting vertex
    heap = [ (0, starting_vertex) ]
    heapq.heapify(heap)
    
    while len(heap) > 0:
        
        print(heap)
        print(distances)
        print()
        
        # return minimum distance vertex from current_vertex
        current_distance, current_vertex = heapq.heappop(heap)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor_vertex, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = distance
                heapq.heappush(heap, (distance, neighbor_vertex))
                
                
    return distances
        
# =============================================================================
#         current_distance, current_vertex = heapq.heappop(pq)
# 
#         # Nodes can get added to the priority queue multiple times. We only
#         # process a vertex the first time we remove it from the priority queue.
#         if current_distance > distances[current_vertex]:
#             continue
# 
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
# 
#             # Only consider this new path if it's better than any path we've
#             # already found.
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
# 
#     return distances
# =============================================================================


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'U'))

