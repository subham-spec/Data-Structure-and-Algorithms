from collections import deque

class DFS:
    def printDFSPath(self, n, edges, source):
        my_dict = {}
        for i in range(1, n+1):
            my_dict[i] = []
        
        for  arr in edges:
            key, val = arr[0], arr[1]
            my_dict[key].append(val)
            my_dict[val].append(key)
        
        print('Graph created is:', my_dict)
        
        print('DFS Traversal is:', end=' ')
        
        visited = [0 for _ in range(n+1)]
        def dfsPath(source):
            visited[source] = 1
            print(source, end=' ')
            for val in my_dict[source]:
                if not visited[val]:
                    dfsPath(val)
        dfsPath(source)

        
if __name__ == "__main__":
    n = 8
    edges = [
                [1,2],[1,3],
                [2,5],[2,6],
                [3,4],[3,7],
                [4,8],
                [7,8]
            ]
    source = 1
    # Calling for the DFS of the path
    DFS().printDFSPath(n, edges, source)
    
