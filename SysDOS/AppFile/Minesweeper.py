import random, time

print('新·扫雷,之前的扫雷有点bug')
print('欢迎来玩由MayOS团队制作的扫雷')
time.sleep(0.6)
print('1.创建一个新游戏')
print('任意键退出游戏')
a = input()
if a == '1':
    pass
else:
    quit()
time.sleep(0.5)
print('请稍后，正在生成地图')
time.sleep(1)
game_map1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
game_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
sum = 0
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(100):
    r = random.randint(1, 6)
    if r == 1:
        game_map[i] = 'x'
        sum += 1
remaining_block = 100 - sum
while True:
    print('有' + str(sum) + '个雷')
    print('    1 2 3 4 5 6 7 8 9 10')
    print()
    for i in range(10):
        print(i + 1, end = '')
        if i <= 9:
            print(end = '   ')
        else:
            print(end = ' ')
        for j in range(10):
            print(game_map1[(i * 10 + j) - 1], end = ' ')
        print()
    print('请输入列号空格行号')
    an = input().split()
    try:
        x = int(an[0])
        y = int(an[1])
    except:
        print('请输入规范的行号, 如 1 1')
        continue
    if len(an) != 2:
        print('请输入规范的行号, 如 1 1')
        continue
    elif x not in number_list or y not in number_list:
        print('请输入规范的行号, 如 1 1')
        continue
    else:
        b = (y - 1) * 10 + x - 1
        print(b)
        if game_map[b] == 'x':
            print('你踩到雷了!')
            print('    1 2 3 4 5 6 7 8 9 10')
            print()
            for i in range(10):
                print(i + 1, end='')
                if i <= 9:
                    print(end='   ')
                else:
                    print(end=' ')
                for j in range(10):
                    print(game_map[(i * 10 + j) - 1], end=' ')
                print()
            time.sleep(5)
            quit()
        else:
            block_list = [-11, -10, -9, -1, 1, 9, 10, 11]
            block_list1 = [-11, -10, -1, 9, 10]
            block_list2 = [-10, -9, 1]
            block_list3 = [-11, -10, -9, -1, 1]
            block_list4 = [-11, -10, -1]
            bomb = 0
            if b <= 88:
                for i in range(8):
                    if game_map[b + block_list[i]] == 'x':
                        bomb += 1
            elif b == 89:
                for i in range(5):
                    if game_map[b + block_list1[i]] == 'x':
                        bomb += 1
            elif b == 90:
                for i in range(3):
                    if game_map[b + block_list2[i]] == 'x':
                        bomb += 1
            elif b >= 91 and b <= 98:
                for i in range(5):
                    if game_map[b + block_list3[i]] == 'x':
                        bomb += 1
            elif b == 99:
                for i in range(3):
                    if game_map[b + block_list4[i]] == 'x':
                        bomb += 1
            if bomb >= 1:
                game_map1[b - 1] = bomb
            else:
                game_map1[b - 1] = 9
            remaining_block -= 1
    if remaining_block == 0:
        print('你赢了!')
        time.sleep(10)
        quit()