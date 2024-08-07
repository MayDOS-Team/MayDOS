import random, time, os

os.system('cls')

print('欢迎使用由MayDOS制作的扫雷游戏.')

ch = input("1-开始游戏\n2-退出游戏\n请选择：")


class MinesweeperTimer:
    def __init__(self):
        self.start_time = None

    def start(self):
        """启动计时器"""
        self.start_time = time.time()

    def stop(self):
        """停止计时器"""
        self.start_time = None  # 重置计时器

    def elapsed_time(self):
        """返回经过的时间（秒），如果计时器未启动则返回 0"""
        if self.start_time is None:
            return 0
        return time.time() - self.start_time

    def formatted_time(self):
        """返回格式化后的时间字符串 x时x分x秒"""
        elapsed_seconds = int(self.elapsed_time())
        hours, remainder = divmod(elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}时{minutes}分{seconds}秒"


timer = MinesweeperTimer()


def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mine_locations = random.sample(range(rows * cols), num_mines)
    for loc in mine_locations:
        row = loc // cols
        col = loc % cols
        board[row][col] = 'X'
    return board


def get_adjacent_mines(board, rows, cols):
    count = 0
    rows = len(board)
    cols = len(board[0])

    for i in range(max(0, rows - 1), min(rows, rows + 2)):
        for j in range(max(0, cols - 1), min(cols, cols + 2)):
            if board[i][j] == 'X':
                count += 1

    return count


def print_board(board):
    rows = len(board)
    cols = len(board[0])

    print('   ', end='')
    for i in range(cols):
        print(f'{i} ', end='')
    print()

    print('  +' + '---' * cols)

    for i in range(rows):
        print(f'{i} |', end='')
        for j in range(cols):
            print(f'{board[i][j]} ', end='')
        print()

    print('  +' + '---' * cols)


def play_game():
    global ch, col, row
    while True:
        if ch == '1':
            game_mode = str(
                input("请选择游戏模式：\n1-初级（Beginner）\n2-中级（Intermediate）\n3-高级（Expert）\n4-自定义（Customized）\n请选择："))
            if game_mode == '1':
                print("你选择了初级（Beginner）模式！\n此模式拥有9行9列，10个地雷")
                rows, cols, num_mines = 9, 9, 10
                print("游戏开始！")
                break

            elif game_mode == '2':
                print("你选择了中级（Intermediate）模式！\n此模式拥有16行16列，40个地雷")
                rows, cols, num_mines = 16, 16, 40
                print("游戏开始！")
                break

            elif game_mode == '3':
                print("你选择了高级（Expert）模式！\n此模式拥有30行16列，99个地雷")
                rows, cols, num_mines = 30, 16, 99
                print("游戏开始！")
                break

            elif game_mode == '4':
                print("你选择了自定义（Customized）模式！\n请输入行数、列数和地雷数量")
                rows = int(input("请输入行数："))
                cols = int(input("请输入列数："))
                num_mines = int(input("请输入地雷数量："))
                if num_mines < rows * cols * 0.15:
                    print("地雷数量不能小于格子总数的15%！")
                    return
                if num_mines > rows * cols * 0.25:
                    print("地雷数量不能大于格子总数的25%！")
                    return
                if num_mines < 1:
                    print("地雷数量不能小于1！")
                    return
                if rows < 1 or cols < 1:
                    print("行数和列数不能小于1！")
                    return
                if rows > 50 or cols > 50:
                    print("行数和列数不能大于50！")
                    return
                print("恭喜你已经完成所有步骤")
                print("你选择了高级（Expert）模式！\n此模式拥有 " + str(rows) + " 行 " + str(cols) + " 列， " + str(num_mines) + " 个地雷")
                print("游戏开始！")
                break

            elif game_mode not in ['1', '2', '3', '4']:
                print("无效的选择，请重新输入")
                return
        elif ch == '2':
            print("游戏结束！")
            exit()
        else:
            print("无效的选择，请重新输入")
            return

    if rows < 1 or cols < 1:
        print("行数和列数不能小于1！")
        exit()
    if rows > 50 or cols > 50:
        print("行数和列数不能大于50！")
        exit()
    if num_mines < 1:
        print("地雷数量不能小于1！")
        exit()

    board = create_board(rows, cols, num_mines)
    visible = [[0 for _ in range(cols)] for _ in range(rows)]

    game_over = False
    # timer.start()

    return board, visible, game_over


re_board, re_visible, re_game_over = play_game()


# 判断游戏是否触雷，如果触雷则结束游戏，否则继续游戏，直到游戏结束，输出最终结果
def game_rule():
    global re_board, re_visible, re_game_over
    board = re_board
    visible = re_visible
    game_over = re_game_over
    while not game_over:
        print_board(visible)
        row = int(input("请输入行号："))
        col = int(input("请输入列号："))
        os.system("cls")

        if board[row][col] == 'X':
            os.system("cls")
            print('游戏结束，您触雷了！')
            game_over = True

        else:
            count = get_adjacent_mines(board, row, col)
            visible[row][col] = str(count)

    print_board(board)


if __name__ == "__main__":
    play_game()
    game_rule()
