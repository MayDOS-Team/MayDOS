import base64
import os
import sys
import time
from time import sleep

import wget


# 彩色自定义文本
class Style:
    END = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    URL = '\33[4m'
    BLINK = '\33[5m'
    BLINK2 = '\33[6m'
    SELECTED = '\33[7m'


class Font:
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'


class Background:
    BLACK = '\33[40m'
    RED = '\33[41m'
    GREEN = '\33[42m'
    YELLOW = '\33[43m'
    BLUE = '\33[44m'
    VIOLET = '\33[45m'
    BEIGE = '\33[46m'
    WHITE = '\33[47m'


# 系统权限API
class SysPerAPI():
    def __init__(self, Per: str = 'sys') -> None:
        self.Per = Per

    def cls(self) -> int:
        try:
            os.system('cls')
            # 尝试执行cls指令，如果是Windows系统则会返回代码200
            return 200
        except Exception as e:
            print(f'{Font.RED}在执行操作时报错：{e}{Font.WHITE}')
            # 如果出错则返回错误代码400
            return 400

    def CreatSysFile(self, path: str = '', context: str = 'Test') -> int:
        try:
            if self.Per == 'sys':
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(f'SYS_FILE\n{context}')
                    f.close()
                    # 如果以上操作完成，则返回200
                    return 200
            elif self.Per != 'sys':
                print(f'{Font.YELLOW}权限不足{Font.WHITE}')
                # 如果权限不足，则返回代码201
                return 201
            else:
                print(f'{Font.YELLOW}Unknown permissions: {self.Per}{Font.WHITE}')
                # 其他问题返回代码202
                return 202
        except Exception as e:
            print(f'{Font.RED}在执行操作时报错：{e}{Font.WHITE}')
            # 如果以上操作出错，则返回错误代码400
            return 400

    def JsonFileRead(self, path):
        try:
            with open(path, 'r') as f:  # 尝试读取path路径的文件，如果顺利完成，则返回文件内容
                __date = f.read()
                f.close()
                return __date
        except Exception as e:  # 如果出错，则显示错误信息
            print(f'{Font.RED}在执行操作时报错：{e}')


def create_dir():  # 创建系统文件夹函数
    DIR_LIST = ['MayDOS_Login/', 'important/', 'important/Applications', 'important/log', 'important/download',
                'important/download/per.txt', '.exe/software.txt']
    for dir in DIR_LIST:
        if dir != DIR_LIST[-1]:
            if not os.path.isdir(dir):
                os.makedirs(dir)
        else:
            if not os.path.isdir(dir):
                with open('important/download/per.txt', 'w') as f:
                    f.write('root')
                    f.close()


def check_ver():  # 检查系统版本文件函数
    try:
        ver_open = open('important/Version.ver', mode='r')
        # 尝试打开系统版本文件
        ver_open.seek(0, 0)
        CODE = ver_open.read()
        # 返回版本号
        return CODE
    except FileNotFoundError as e:
        print(
            f'{Font.RED}错误信息：{e}\n系统版本文件被移动或异常丢失，请尝试联系我们以修复,可尝试启动OOBE修复{Font.WHITE}')
        # 错误则输出错误信息和提示
        input('按下回车键退出. . .')
        quit()


def check_user_login():  # 检查用户登录函数
    try:
        account_open = open('important/account.user', mode='r')
        # 尝试打开用户文件并读取到accout_info变量中
        account_info = account_open.readlines()

        un_username = account_info[0]
        username = un_username[0:-1]
        # 读取用户名

        un_password = account_info[1]
        password = un_password[0:-1]
        # 读取用户密码

        account_open.close()
        # 养成关闭文件的良好习惯:)

        try:
            username = str(base64.b64decode(username), 'utf-8')
            password = str(base64.b64decode(password), 'utf-8')
            # 尝试对用户名和密码进行base64解码
        except Exception as e:
            print(f'{Font.RED}ERROR: 账户信息加载失败，账户文件可能损坏，请尝试注销并重新注册{Font.WHITE}')
            print(f'{Font.RED}错误信息：{e}{Font.WHITE}')
            input('按下回车键退出. . .')
            quit()
        # 不出错则会返回用户信息，用户名和用户密码
        return account_info, username, password

    except FileNotFoundError:
        print(f'{Font.RED}未注册或账户文件异常丢失,可尝试启动OOBE修复{Font.WHITE}')
        # 如果文件找不到则判定为账户未注册或账户文件异常丢失
        input('按下回车键退出. . .')
        quit()


def user_login(account_info, username, password):
    while True:
        try:
            match username:  # match -- case为Python3.10及以上语法，如果此处报错则为Python版本过低
                case "TEST":  # 测试账户则直接通过
                    print(account_info)
                    print(f'{Font.BLUE}测试账户登录{Font.WHITE}')
                    break
                case _:
                    print(f'{Font.BEIGE}登录{username}的电脑{Font.WHITE}')
                    userspassword = input('密码>')
        except Exception as e:
            # 提示用户更新Python
            print("{Font.RED}错误信息：{e}\nPython版本过低，请使用3.10以上版本{Font.WHITE}")
            input("按任意键退出. . .")
            quit()
        # 判断密码是否正确
        if userspassword == password:
            print(f'{Font.GREEN}密码正确{Font.WHITE}')
            break
        else:
            print(f'{Font.RED}密码错误！{Font.WHITE}')
            pass


def notepad():
    try:
        ENCO_FILE = 'w'

        print('\n选择编辑模式 -->')
        print('1.正常写入')
        print('2.系统权限写入')
        print('3.特殊文件写入')

        print(f'{Font.YELLOW}================')
        print(f'{Font.BEIGE}exit        退出')
        print(f'{Font.BEIGE}path    文件路径{Font.WHITE}\n')
        print(f'{Font.BEIGE}enco    读取方式{Font.WHITE}\n')

        match input('MayDOS/Apply/NOTEPAD>>>'):
            case 'exit':
                print('\n')
            case '1':
                print(f'模式:正常写入\n')
                CFILE = input("MayDOS/Apply/NOTEPAD/CreatFile>>>")
                with open(CFILE, ENCO_FILE, encoding='utf-8') as f:
                    # 向文件写入用户输入的内容
                    f.write(CFILE)
                    f.close()
            # SysPerAPI().cls()
            # os.system('python important/Applications/Notepad/Notepad.py')
            # 墓前上面两个语句出问题了，所以注释掉

    except Exception as e:
        print(f'{Font.RED}在执行操作时报错：{e}{Font.WHITE}')
        # 如果出错则输出错误信息（大部分可能是match -- case的问题，恼）


def sof(cmd):
    try:
        if cmd.endswith('json'):
            # 我也不知道为什么是json就无权，恼
            print(f"{Font.RED}该文件您无权访问")
        elif cmd.endswith('api') or cmd.endswith('api.py'):
            # 这个我也不知道（恼
            print(f"{Font.RED}该文件您无权访问")
        else:
            if not os.stat(f'{os.path.abspath(f"important/Applications_tmp/{cmd}")}').st_size == \
                   os.stat(f'{os.path.abspath(f"important/Applications/{cmd}")}').st_size:
                match input(f'安全提醒：{Font.YELLOW}应用程序"{cmd}"可能已被恶意篡改,请谨慎运行。（Y/N){Font.WHITE}').lower():
                    case "y" | "yes":
                        try:
                            os.system(f'START /MAX {os.path.abspath(f"important/Applications/{cmd}")}')
                        except Exception as e:
                            # 为什么这个语句会出错呢，我也不知道
                            print(f'{Font.RED}{e}')
                    case _:
                        pass
            else:
                try:
                    os.system(f'START /MAX {os.path.abspath(f"important/Applications/{cmd}")}')
                except Exception as e:
                    # 为什么这个语句会出错呢，我也不知道
                    print(f'{Font.RED}{e}')

    except Exception as e:
        print(f'{Font.RED}{e}')


def download():
    print("=======================================")
    print(
        "|请选择下载源                         |            \n|1.STORE 默认的应用商店 2.HTTP网络渠道|\n|3.退出                           "
        "    |")
    print("=======================================")
    match input("MayDOS/download>>>"):
        case '1':
            # 没啥用的1
            print("======================================================")
            print("已选择下载源<STORE>,可下载已上传的应用,输入EXIT以退出|")
            print("======================================================")
            while True:
                if input("MayDOS/Download/STORE>>>").lower() == 'exit':
                    break

        case '2':
            # 下载文件
            print("=========================================================")
            print("已选择下载源<HTTP>,可下载任何网络上的应用,输入EXIT以退出|")
            print("=========================================================")
            while True:
                D_I_0 = input("MayDOS/Download/HTTP>>>")
                # 判断输入的内容，非exit就下载文件到download文件夹
                if D_I_0.lower() == 'exit':
                    break
                else:
                    try:
                        wget.download(f'{D_I_0}', "important/download/")
                    except ValueError:
                        pass

        case _:
            # 我也不道啊
            print("未知操作,已自动退出......")
            print("===================================================")


class Progressbar:
    def __init__(self, message, mode, sleep_time):
        self.mode = mode
        self.message = message
        self.sleep_time = sleep_time

    def start(self):
        if self.mode == 0:
            for i in range(1, 101):
                print('\r', end="")
                print(str(self.message), f"{i}%", "▌" * (i // 2), end='')
                sys.stdout.flush()
                sleep(self.sleep_time)  # 刷新输出区，否则以上进度条不会立马显示
        if self.mode == 1:
            for i in range(1, 101):
                print('\r', end="")
                print(str(self.message), f"{i}%", "▋" * (i // 2), end='')
                sys.stdout.flush()
                sleep(self.sleep_time)  # 刷新输出区，否则以上进度条不会立马显示


def menu(cmd):
    a = open(".exe/software.txt", "r", encoding="utf-8").read().split("\n")
    if cmd.lower() in a:
        return "系统软件"
    else:
        return "第三方软件"


def cmd(cmd):
    os.system(cmd)


def ls(cmd):
    a = os.listdir(os.path.abspath(cmd))
    for o in range(len(a)):
        a[o] = a[o] + f"\t<{time.ctime(os.path.getctime(os.path.abspath(cmd)))}>"
    return a


def reload():
    os.system("start MayDOS_System.py")

    
    
