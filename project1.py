N = int(input("N: "))
arr = []

for i in range(N):
    min_map = input(":")
    arr.append(list(map(int, min_map.split())))

def count_mines(row, col):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < N and 0 <= c < N and arr[r][c] == 1:
                count += 1
    return count

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            print("*", end=" ")
        else:
            mine_count = count_mines(i, j)
            print(mine_count, end=" ")
    print()