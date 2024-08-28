dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
TARGET_SUM = 100

def find_dwarf(dwarfs):
    total_sum = sum(dwarfs)
    for i in range(9):
        for j in range(i+1, 9):
            if total_sum - dwarfs[i] - dwarfs[j] == TARGET_SUM:
                return [dwarfs[k] for k in range(9) if k != i and k != j]

result = find_dwarf(dwarfs)
for r in result:
    print(r)