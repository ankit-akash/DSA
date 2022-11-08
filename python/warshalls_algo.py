n=int(input("Enter the number of nodes:"))
cost=[[0 for i in range(n)] for j in range(n)]
print("Enter the adjacency matrix in integers:")
for i in range(n):
 for j in range(n):
 temp=int(input())
 cost[i][j]=temp
print("The adjacency matrix in integers:")
for i in range(n):
for j in range(n):
 if cost[i][j]==999:
 print("INF",end="\t")
 else:
 print(cost[i][j],end="\t")
 print("\n")
for k in range(n):
 for i in range(n):
 for j in range(n):
 cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
print("*******FLOYD WARSHALL********")
for i in range(n):
 for j in range(n):
 if cost[i][j]==999:
 print("INF",end="\t")
 else:
 print(cost[i][j],end="\t")
 print("\n")
