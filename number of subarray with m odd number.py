def CountSubArray(a,n,m):
	count=0
	prefix=[0]*n
	odd=0
	for i in range(n):
		prefix[odd]=prefix[odd]+1

		if(a[i]%2):
			odd+=1
		if(odd>=m):
			count=count+prefix[odd-m]
	return count