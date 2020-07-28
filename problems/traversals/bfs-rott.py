from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows < 1:
            return 0
        cols = len(grid[0])
        if cols <1:
            return 0
        
        #rotten = [(i,j) for j in range(cols)for i in range(rows) if grid[i][j] == 0] 
        directions =[(1,0),(0,1),(-1,0),(0,-1)]
        q =deque()
        rotten =0
        empties = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==2:
                    q.append((i,j))
                    rotten+=1
                if grid[i][j] == 0:
                    empties+=1
        time = 0
        
        while len(q) > 0:
            size = len(q)
            while size > 0:
                front = q.popleft()
                size-=1

                for _,d in enumerate(directions):
                    next = (front[0]+d[0], front[1]+d[1])
                    if next[0] < 0 or next[0] >= rows:
                        continue
                    if next[1] < 0 or next[1] >= cols:
                        continue
                    if grid[next[0]][next[1]] == 0 or grid[next[0]][next[1]] == 2 :
                        continue
                    
                    q.append(next)
                    grid[next[0]][next[1]] = 2
                    rotten +=1
            if len(q) > 0:time+=1
        
        if rotten == rows*cols - empties:
            return time
        return -1

