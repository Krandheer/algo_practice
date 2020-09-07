class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans=0
        obstacleSet=set(map(tuple, obstacles))
        
        #i can move up by default, if -1 then i can move in +x,
        #if i am moving in positive x then if -2 then I can move
        #up or if -1 then I have to move downwards, basically I have all
        #4 choices available to move starting from facing up.
        x=0
        y=0
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        di=0
        
        for cmd in commands:
            if cmd == -2:
                #I have to turn to left direction at 90 degree from current direction
                
                di = (di-1)%4
            
            elif cmd==-1:
                #I have to turn right 90 degree from current position
                
                di = (di+1)%4
            
            else:
                #I have to move forward in the direction I have been looking                           #towards
                for i in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x=x+dx[di]
                        y=y+dy[di]
                        
                        ans =max(ans, x**2+y**2)
        return ans
                        
        