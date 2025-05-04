import sys

def min_key(key, in_mst, V):
    min_val = sys.maxsize
    min_index = -1

    for v in range(V):
        if not in_mst[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def prim_mst(graph, V):
    key = [sys.maxsize] * V  # To store minimum edge weight
    parent = [None] * V      # To store MST structure
    in_mst = [False] * V     # To track vertices included in MST

    key[0] = 0
    parent[0] = -1  # First node is root of MST

    for _ in range(V - 1):
        u = min_key(key, in_mst, V)
        in_mst[u] = True

        for v in range(V):
            if graph[u][v] and not in_mst[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    # Print the MST
    print("Edge \tWeight")
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

def main():
    V = int(input("Enter number of vertices: "))
    graph = []

    print("Enter adjacency matrix (use 0 for no edge):")
    for _ in range(V):
        row = list(map(int, input().split()))
        graph.append(row)

    print("\nMinimum Spanning Tree using Prim's Algorithm:")
    prim_mst(graph, V)

if __name__ == "__main__":
    main()
