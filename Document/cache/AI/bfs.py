from collections import deque

# Recursive BFS helper function
def bfs_recursive(q, adj_list, visited):
    if not q:
        return

    current = q.popleft()
    print(f"Visited: {current}")

    for neighbor in adj_list[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append(neighbor)

    bfs_recursive(q, adj_list, visited)  # Recursive call


def main():
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    adj_list = [[] for _ in range(num_vertices)]
    visited = [False] * num_vertices

    print("Enter edges (format: u v for undirected edge between u and v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)  # Undirected graph

    start_vertex = int(input("Enter starting vertex for BFS: "))
    q = deque()
    visited[start_vertex] = True
    q.append(start_vertex)

    print(f"Breadth First Search starting from vertex {start_vertex}:")
    bfs_recursive(q, adj_list, visited)


if __name__ == "__main__":
    main()
