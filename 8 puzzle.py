from heapq import heappop, heappush

goal = [[1,2,3],[4,5,6],[7,8,0]]
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def h(s):
    return sum(abs((v-1)//3 - i) + abs((v-1)%3 - j)
               for i in range(3) for j in range(3) if (v := s[i][j]))

def blank(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0: return i, j

def inside(x, y): return 0 <= x < 3 and 0 <= y < 3

def astar(start):
    heap, seen = [(h(start), start, [])], set()
    while heap:
        _, curr, path = heappop(heap)
        if curr == goal: return path + [curr]
        key = tuple(map(tuple, curr))
        if key in seen: continue
        seen.add(key)
        x, y = blank(curr)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if inside(nx, ny):
                new = [r[:] for r in curr]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                heappush(heap, (h(new) + len(path) + 1, new, path + [curr]))

start = [[1,2,3],[4,0,6],[7,5,8]]
res = astar(start)
for step in res:
    print(*step, sep="\n"); print()

