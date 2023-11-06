import time


def win(L):
    if L[1][1:4] == ['x', 'x', 'x'] or L[2][1:4] == ['x', 'x', 'x'] or L[3][1:4] == ['x', 'x', 'x'] or [L[i][4-i] for i in range(1, 4)] == ['x', 'x', 'x'] or [L[i][i] for i in range(1, 4)] == ['x', 'x', 'x']:
        print('Победа крестиков!')
        return True
    if L[1][1:4] == ['o', 'o', 'o'] or L[2][1:4] == ['o', 'o', 'o'] or L[3][1:4] == ['o', 'o', 'o'] or [L[i][4-i] for i in range(1, 4)] == ['o', 'o', 'o'] or [L[i][i] for i in range(1, 4)] == ['o', 'o', 'o']:
        print('Победа ноликов!')
        return True
    for j in range(1, 4):
        a = [L[i][j] for i in range(1, len(L))]
        if a == ['x', 'x', 'x']:
            print('Победа крестиков!')
            return True
        if a == ['o', 'o', 'o']:
            print('Победа ноликов!')
            return True
    if '-' not in [L[j][i] for j in range(1, 4) for i in range(1, 4)]:
        print('Ничья!')
        return True
    return False

print('Ход - это x или o (через английскую раскладку)')
lst = [[' ', '0', '1', '2'],
       ['0', '-', '-', '-'],
       ['1', '-', '-', '-'],
       ['2', '-', '-', '-']]

cross = 0
zero = 0
for step in range(10**9):
    prnt = [' '.join(lst[i]) for i in range(len(lst))]
    print(*prnt, sep='\n')
    print('Введите строку, столбец и ход игрока через пробел')

    pack = list(map(str, input().split()))
    if len(pack) != 3:
        print('Неправильно введён ход')
        continue
    a, b, w = pack[0], pack[1], pack[2]
    a = int(a) + 1
    b = int(b) + 1
    if not(1 <= a <= 3) or not(1 <= b <= 3):
        print('Неправильно введён ход')
        continue
    if not(w == 'x' or w == 'o'):
        print('Неправильный ход!')
        continue
    if lst[a][b] != '-':
        print('Позиция занята!')
        continue
    if w == 'x':
        cross += 1
    if w == 'o':
        zero += 1
    if cross - zero == 2:
        cross -= 1
        print('Ход другого игрока!')
        continue
    if zero > cross:
        zero -= 1
        print('Ход другого игрока!')
        continue

    lst[a][b] = w

    if win(lst):
        prnt = [' '.join(lst[i]) for i in range(len(lst))]
        print(*prnt, sep='\n')
        break

time.sleep(5)
