N, K = map(int, input().split())
times = list(map(int, input().split()))

flag = True

max_ind = times.index(max(times))
max_1 = times[max_ind]
max_indecs = []

for i in range(max_ind, N):
    if(times[i] == max_1):
        max_indecs.append(i)

for i in max_indecs:
    if (flag):
        for j in max_indecs:
            if (i == j):
                continue
            elif (abs(j - i) > K - 1):
                print(max_1 * 2)
                flag = False
                break


if (flag):
    max_2 = 0
    max_ind_2 = 0
    for ind in max_indecs:
        for i in range(len(times)):
            if (i == ind):
                continue
            elif ((times[i] > max_2) and (abs(ind - i) > K - 1)):
                max_2 = times[i]
                max_ind_2 = i
    if(max_2 != 0):
        print(max_1 + max_2)
        flag = False


if (flag):
    max_sum = 0
    for i in range(N - K):
        edge = i + K
        if(edge != N):
            j = max(times[edge : N])
            s = times[i] + j
            if (s > max_sum):
                max_sum = s
    print(max_sum)
