def get_biggest_region(grid):
    n = len(grid)
    m = len(grid[0])

    def neighbors(i, j):
        result = []
        if i != 0:
            result.append((i - 1, j))
            if j != 0:
                result.append((i - 1, j - 1))
            if j != m - 1:
                result.append((i - 1, j + 1))
        if i != n - 1:
            result.append((i + 1, j))
            if j != 0:
                result.append((i + 1, j - 1))
            if j != m - 1:
                result.append((i + 1, j + 1))
        if j != 0:
            result.append((i, j - 1))
        if j != m - 1:
            result.append((i, j + 1))
        return result

    # Each island
    islands = []

    def unExplored(i, j):
        for island in islands:
            if (i, j) in island:
                return False
        return True

    def dfsWithSize(i, j):
        visited = set()

        def dfs(i, j):
            if grid[i][j] == 0:
                return
            visited.add((i, j))
            for di, dj in neighbors(i, j):
                if (di, dj) not in visited:
                    dfs(di, dj)

        dfs(i, j)

        islands.append(visited)
        return

    for i in range(n):
        for j in range(m):
            if unExplored(i, j):
                dfsWithSize(i, j)


    return max(map(lambda island: len(island), islands))


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
