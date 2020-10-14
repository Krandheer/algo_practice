def dfs(s):
	global visited, alist, valCount
	visited[s]=1
	l = len(alist[s])
	valCount=valCount+1
	if(l!=0):
		for i in range(l):
			if(visited[alist[s][i]]==0):
				dfs(alist[s][i])

	q=int(raw_input().split())
	valCount=0
	for a0 in range(q):
		n,m,clib,croad=map(int, raw_input().split())
		visited=[0 for i in range(n+1)]
		alist=[[] for i in range(n+1)]
		count=0
		roads=0
		road=[]
		current=0
		for a1 in range(m):
			city1,city2=map(int, raw_input().split(' '))
			alist[city1].append(city2)
			alist[city2].append(city1)
		if(m==0 or corad>=clib):
			print(n*clib)
		else:
			for i in range(1,n+1):
				if(visited[i]==0):
					valCount==0
					dfs(i)
					road.append(valCount)
				ans=0
				p=len(road)

				for i in range(p):
					ans = ans+min((road[i]-1)*croad + clib, road[i]*clib)

				print(ans)