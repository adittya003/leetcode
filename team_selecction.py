def max_team_expertise(n, c, conflicts, expertise):
    graph = [[] for _ in range(n + 1)]

    for conflict in conflicts:
        a, b = conflict
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, visited):
        visited[node] = True
        total_expertise = expertise[node - 1]

        for neighbor in graph[node]:
            if not visited[neighbor]:
                total_expertise += dfs(neighbor, visited)

        return total_expertise

    visited = [False] * (n + 1)
    max_expertise = 0

    for i in range(1, n + 1):
        if not visited[i]:
            max_expertise = max(max_expertise, dfs(i, visited))

    return max_expertise

# Reading input
n, c = map(int, input().split())
conflicts = [tuple(map(int, input().split())) for _ in range(c)]
expertise = list(map(int, input().split()))

# Output
result = max_team_expertise(n, c, conflicts, expertise)
print(result)
