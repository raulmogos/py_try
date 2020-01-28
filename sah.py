

def main():
    
    table = []
    for i in range(8):
        table.append([0,0,0,0,0,0,0,0])

    table[0][0] = 1
        
    steps = [[1,2], [2,1], [-1,2], [2,-1]]

    points = [[0,0]]

    sw = True
    start = 0
    
    while sw:
        
        if [7,7] in points:
            sw = True
            break

        l = []
        for p in points:
            for step in steps:
                i = p[0] + step[0]
                j = p[1] + step[1]
                if (i <= 7 and i >= 0) and (j <= 7 and j >= 0) and table[i][j] == 0:
                    table[i][j] = 1
                    l.append([i, j])
        points = l

    for t in table:
        print(t)

    revers_table = []
    for _ in range(8):
        revers_table.append([0,0,0,0,0,0,0,0])

    print()
    for i in range(8):
        for j in range(8):
            revers_table[7 - i][7 - j] = table[i][j]

    for t in revers_table:
        print(t)

    last = []
    for _ in range(8):
        last.append([0,0,0,0,0,0,0,0])
        
    for i in range(8):
        for j in range(8):
            last[i][j] = table[i][j] and revers_table[i][j]

    print()
    
    for t in last:
        print(t)

main()













