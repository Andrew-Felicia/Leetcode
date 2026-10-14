########################################################################################################
########################---------Solution: writen by codex--------######################################
# import sys


# def main():
#     data = list(map(int, sys.stdin.buffer.read().split()))
#     if not data:
#         return

#     index = 0
#     required_memory = data[index]
#     index += 1

#     tensor_count = data[index]
#     index += 1

#     sizes = data[index:index + tensor_count]
#     index += tensor_count

#     swap_costs = data[index:index + tensor_count]
#     index += tensor_count

#     recompute_costs = data[index:index + tensor_count]

#     if sum(sizes) < required_memory:
#         print("error")
#         return

#     costs = [
#         min(swap_costs[i], recompute_costs[i])
#         for i in range(tensor_count)
#     ]

#     infinity = float("inf")

#     # dp[freed] is the minimum cost needed to free `freed` memory.
#     # required_memory also represents every result greater than the target.
#     dp = [infinity] * (required_memory + 1)
#     dp[0] = 0

#     reachable = 0

#     for size, cost in zip(sizes, costs):
#         # Descending order ensures this tensor is used at most once.
#         for freed in range(reachable, -1, -1):
#             if dp[freed] == infinity:
#                 continue

#             next_freed = min(required_memory, freed + size)
#             candidate_cost = dp[freed] + cost

#             if candidate_cost < dp[next_freed]:
#                 dp[next_freed] = candidate_cost

#         reachable = min(required_memory, reachable + size)

#     if dp[required_memory] == infinity:
#         print("error")
#     else:
#         print(dp[required_memory])


# if __name__ == "__main__":
#     main()

########################################################################################################




import sys

def main():
    data = sys.stdin.readline
    m = int(data())
    n = int(data())
    sizes = list(map(int, data().split()))
    swap_cost = list(map(int, data().split()))
    recompute_cost = list(map(int, data().split()))

    if sum(sizes) < m:
        print("error")
        return
    costs = [min(s, r) for s, r in zip(swap_cost, recompute_cost) ]
    #print(costs)

    #dp[i] means : the minimun costs to reach size i
    dp = [float('inf')] * (m + 1)
    dp[0] = 0

    reachable = 0
    for cost, size in zip(costs, sizes):
        for freed in range(reachable, -1, -1):
            if dp[freed] == float('inf'):
                continue
            next_freed = min(m, size + freed) # prevent index out of bound.
            candidate_cost = cost + dp[freed]
            if candidate_cost < dp[next_freed]:
                dp[next_freed] = candidate_cost
        reachable = min(m, size + reachable)

    if dp[m] == float('inf'):
        print("error")
    else:
        print(dp[m])





if __name__ == "__main__":
    main()