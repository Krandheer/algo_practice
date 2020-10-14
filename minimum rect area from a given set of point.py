import collections 
def minAreaRect(A): 
    columns = collections.defaultdict(list) 
    for x, y in A: 
        columns[x].append(y) 
  
    lastx = {} 
    ans = float('inf') 
  
    for x in sorted(columns): 
        column = columns[x] 
        column.sort() 
        for j, y2 in enumerate(column): 
            for i in range(j): 
                y1 = column[i] 
                # check if rectangle can be formed 
                if (y1, y2) in lastx: 
                    ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1)) 
                lastx[y1, y2] = x 
  
    if ans < float('inf'): 
        return ans 
    else: 
        return 0
  
# Driver code 
A = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]] 
print(minAreaRect(A)) 