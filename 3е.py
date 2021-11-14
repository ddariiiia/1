N, M = map(int, input().split())
weight = [int(i) for i in input().split()] 
cost = [int(i) for i in input().split()]   
weight.insert(0, 0)
cost.insert(0, 0)
A = []
for i in range(N+1):
    A.append([0]*(M+1))
          
for n in range(1, N+1):
    for m in range(M+1):
        A[n][m] = A[n-1][m]
        if (m >= weight[n] and A[n-1][m-weight[n]] + cost[n] > A[n][m]):
            A[n][m] =  A[n-1][m-weight[n]] + cost[n]

def print_answer(n, m):
              if A[n][m] == 0:
                  return
              elif A[n-1][m] == A[n][m]:
                  print_answer(n-1, m)
              else:
                  print_answer(n-1, m - weight[n])
                  print(n)
print_answer(N,M)
