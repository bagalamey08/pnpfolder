# Recursive DFS function
def dfs(vertex, adj_list, visited):
    visited[vertex] = True
    print(f"Visited: {vertex}")

    for neighbor in adj_list[vertex]:
        if not visited[neighbor]:
            dfs(neighbor, adj_list, visited)

def main():
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    # Initialize graph
    adj_list = [[] for _ in range(num_vertices)]
    visited = [False] * num_vertices

    print("Enter edges (format: u v for undirected edge between u and v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)  # undirected graph

    start_vertex = int(input("Enter starting vertex for DFS: "))

    print(f"Depth First Search starting from vertex {start_vertex}:")
    dfs(start_vertex, adj_list, visited)

if __name__ == "__main__":
    main()
