l1=list(map(int,input().split()))
l2=[]
for i in l1:
		if i not in l2:
			l2.append(i)
for i in l2:
		print(i,end=' ')



