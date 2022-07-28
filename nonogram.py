# 코딩중...

import sys; input=sys.stdin.readline

def make_set(lists, index_size, alt_index_size, Stage, flag):
    for i in range(index_size):
        rest_of_sum = alt_index_size - (sum(lists[i]) + len(lists[i]) - 1)
        e = 0
        for element in lists[i]:
            for t in range(element):
                if t >= rest_of_sum:
                    if flag == 'R':
                        Stage[i][e] = 1
                    else:
                        Stage[e][i] = 1
                e += 1
            e += 1

def free_end(R, C, Rows, Columns, Stage, Rows_start_end, Columns_start_end):
    for i in range(R):
        if Rows[i]:
            flag = 'not_first'
            if Stage[i][0] == 1:
                flag = 'free_first'
            for x in range(Rows[i][0]):
                if Stage[i][x] == 1 and flag == 'not_first':
                    flag = 'ok'
                if flag == 'free_first' or flag == 'ok':
                    Stage[i][x] = 1
            if flag == 'free_first':
                Stage[i][Rows[i][0]] = 'X'
                Rows_start_end[i][0] = Rows[i][0] + 1
                Rows[i].pop(0)
        if Rows[i]:
            flag = 'not_first'
            if Stage[i][-1] == 1:
                flag = 'free_first'
            for x in range(R-1, R - Rows[i][-1] - 1, -1):
                if Stage[i][x] == 1 and flag == 'not_first':
                    flag = 'ok'
                if flag == 'free_first' or flag == 'ok':
                    Stage[i][x] = 1
            if flag == 'free_first':
                Stage[i][R - Rows[i][-1] - 1] = 'X'
                Rows_start_end[i][1] = R - Rows[i][-1] - 2
                Rows[i].pop()
    for i in range(C):
        if Columns[i]:
            flag = 'not_first'
            if Stage[0][i] == 1:
                flag = 'free_first'
            for x in range(Columns[i][0]):
                if Stage[x][i] == 1 and flag == 'not_first':
                    flag = 'ok'
                if flag == 'free_first' or flag == 'ok':
                    Stage[x][i] = 1
            if flag == 'free_first':
                Stage[Columns[i][0]][i] = 'X'
                Columns_start_end[i][0] = Columns[i][0] + 1
                Columns[i].pop(0)
        if Columns[i]:
            flag = 'not_first'
            if Stage[-1][i] == 1:
                flag = 'free_first'
            for x in range(C-1, C - Columns[i][-1] - 1, -1):
                if Stage[x][i] == 1 and flag == 'not_first':
                    flag = 'ok'
                if flag == 'free_first' or flag == 'ok':
                    Stage[x][i] = 1
            if flag == 'free_first':
                Stage[R - Columns[i][-1] - 1][i] = 'X'
                Columns_start_end[i][0] = R - Columns[i][-1] - 2
                Columns[i].pop()
            
def main():
    print('노노그램의 규격을 행, 열 순으로 입력하세요.')
    R, C = map(int, input().split())
    Stage = [[0] * C for i in range(R)]
    Rows, Columns = [], []
    Rows_start_end = [[0, C-1] for i in range(R)]
    Columns_start_end = [[0, R-1] for i in range(C)]

    print()
    print('각 행의 값을 위에서부터 입력하세요.')
    for i in range(R):
        Rows.append(list(map(int, input().split())))

    print()
    print('각 열의 값을 왼쪽에서부터 입력하세요.')
    for i in range(C):
        Columns.append(list(map(int, input().split())))
    
    # 확실한 첫 단추
    make_set(Rows, R, C, Stage, 'R')
    make_set(Columns, C, R, Stage, 'C')

    # 양 끝단으로부터 채울 수 있는 것 전부 채우기
    free_end(R, C, Rows, Columns, Stage, Rows_start_end, Columns_start_end)
    
    # 각 range에서 확실한 부분 채우기
    for i in range(R):
        full_flag = 'first_time'
        t = 100
        index = 0
        for element in Rows[i]:
            for _ in range(element):
                if Stage[i][index] == 0:
                    Stage[i][index] = t
                    
                index += 1
            t += 1
    
    
    
    for i in range(R):
        print(*Stage[i])
    for i in range(R):
        print(*Rows_start_end[i])

if __name__ == "__main__":
    main()
