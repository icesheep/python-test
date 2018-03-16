def add(n):
	return add_tail(n,1)
def add_tail(n,m):
	if(n==1):
		return m
	return add_tail(n-1,n*m)