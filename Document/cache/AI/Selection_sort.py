def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Greedily find the index of the minimum element
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print current state of array after each pass
        print(f"Step {i + 1}: {' '.join(map(str, arr))}")

def main():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    print("Sorting using Greedy Selection Sort...")
    selection_sort(arr)

    print("Sorted array:")
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()
