from collections import deque 

T = int(input())

for _ in range(T):
    L = int(input())
    chess = [[0] * L for _ in range(L)]
    current_i, current_j = map(int, input().split())
    want_i, want_j = map(int, input().split())
    
    chess[current_i][current_j] = 1
    
    dx = [-1, 1, -2, 2, -2, 2, -1, 1]
    dy = [-2, -2, -1, -1, 1, 1, 2, 2]
    
    result = 0  
    
    queue = deque()
    queue.append((current_i, current_j, 0))
    
    while queue:
        temp = queue.popleft()
        
        if temp[0] == want_i and temp[1] == want_j:
            print(temp[2])
            break
        
        for i in range(8):
            next_i = dx[i] + temp[0]
            next_j = dy[i] + temp[1]
            
            if 0 <= next_i < L and 0 <= next_j < L and chess[next_i][next_j] == 0:
                chess[next_i][next_j] = 1
                queue.append((next_i, next_j, temp[2]+1))