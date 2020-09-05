class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        MAX = 100
        INT_MAX = (2**32) 
        m=len(matrix)
        n=len(matrix[0])
        dist=[[0 for i in range(MAX)] for i in range(MAX)]
        
        newx=[-1,0,1,0]
        newy=[0,-1,0,1]
        q=[]
        for i in range(m):
            for j in range(n):
                dist[i][j]=INT_MAX
                if(matrix[i][j]==1):
                    dist[i][j]==0
                    q.append([i,j])
                    
        popped=[]
        while(len(q)):
            popped=q[0]
            x=popped[0]
            y=popped[1]
            
            for i in range(4):
                adjx=x+newx[i]
                adjy=y+newy[i]
                
            if (adjx >= 0 and adjx < m and adjy >= 0 and 
                adjy < n and dist[x][y]+1<dist[adjx][adjy]):
                dist[adjx][adjy]=dist[x][y]+1
                q.append([adjx,adjy])
                
        return dist
            
            
            
            
            
            
            
                
                