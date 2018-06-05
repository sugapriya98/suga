x=int(input())
y=[]
for i in range(0,x):
	b=int(input())
	y.append(b)
print(y)
k=int(input())
sum=0
for j in range(0,k):
	sum+=y[j]
print(sum)	
