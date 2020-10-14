def distSumRec(arr,n,sum,currIndex, s):
	if(currIndex>n):
		return
	if(currIndex==n):
		s.add(sum)
		return
	distSumRec(arr,n,sum+arr[currIndex], currIndex+1,s)
	distSumRec(arr,n,sum, currIndex+1,s)


def printDistSum(arr,n):
	s=set()
	def distSumRec(arr,n,0,0,s)
	for i in s:
		print(i, end=' ')