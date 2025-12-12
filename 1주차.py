# 별찍기 1
# a = int(input())
# for i in range(1,a+1):
#     print(i * ('*'))

# 별찍기 2
# a = int(input())
# for i in range(a):
#     print((' '*(a-i)) + ('*'*i))

# X보다 작은 수
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# answer = []
# for i in range(len(A)):
#     if A[i] < X:
#         answer.append(A[i])
# print(*answer)

# X보다 작은 수
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# for i in range(N):
#     if A[i] < X:
#         print(A[i], end=" ")
#     else:
#         pass

# 개수 세기
# N = int(input())
# A = list(map(int, input().split()))
# v = int(input())
# print(A.count(v))

# answer = []
# for i in A:
#   if A[i] < X:
#       answer.append(i)
# print(*answer)

# print(N + X)


# 스위트콘
# N = int(input())
# def vat_calculate(N):
#     return N * (10/11)
# print(int(vat_calculate(N)))

# a = [1, 2, 3, 4, 5, 5]
# print(*a, sep='')