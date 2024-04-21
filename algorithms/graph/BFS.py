from collections import deque

class BFS:
    def printBFSPath(self, n, edges, source):
        my_dict = {}
        for i in range(1, n+1):
            my_dict[i] = []
        
        for  arr in edges:
            key, val = arr[0], arr[1]
            my_dict[key].append(val)
            my_dict[val].append(key)
        
        print('Graph created is:', my_dict)
    
        queue = deque()
        queue.append(source)
        visited = [0 for _ in range(n+1)] 
        # or other way of creating this is --> [0]*(n+1)
        
        print('BFS Traversal is:', end=' ')
        while queue:
            front = queue[0]
            queue.popleft()
            if visited[front] == 1:
                continue
            visited[front] = 1
            arr = my_dict[front]
            print(front, end=' ')
            for val in arr:
                queue.append(val)
                
        return False

if __name__ == "__main__":
    n = 8
    edges = [
                [1,2],[1,6],
                [2,3],[2,4],
                [4,5],
                [5,7],
                [6,7],[6,8],
            ]
    source = 1
    # Calling for the BFS of the path
    BFS().printBFSPath(n, edges, source)
    
