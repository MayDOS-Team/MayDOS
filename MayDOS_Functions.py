try:
    import wget, json, requests
    import os, sys, asyncio, tkinter.messagebox
    import base64
except Exception as e:
    print(f"{e}\n")
    os.system(r'install.bat')
    os.system(r'cls')
    quit()

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
    def __init__(self,Per : str = 'sys') -> None:
        self.Per = Per
        return None

    def cls(self) -> int:
        try:
            os.system('cls')
            return 200
        except Exception as e:
            print(f'{Font.RED}MayDOS/ROOT/ERROR>>>{e}{Font.WHITE}')
            return 400

    def CreatSysFile(self,path : str = '',context : str = 'Test') -> int:
        try:
            if self.Per == 'sys':
                with open(path,'w',encoding='utf-8') as f:
                    f.write(f'SYS_FILE\n{context}')
                    f.close()
                return 200
            elif self.Per != 'sys':
                print(f'{Font.YELLOW}权限不足{Font.WHITE}')
                return 201
            else:
                print(f'{Font.YELLOW}Unknown permissions: {self.Per}{Font.WHITE}')
                return 202
        except Exception as e:
            print(f'{Font.RED}MayDOS/Root/ERROR>>>{e}{Font.WHITE}')
            return 400

    def JsonFileRead(self,path):
        try:
            with open(path,'r') as f:
                __date = f.read()
                f.close()
                return __date
        except Exception as e:
            print(f'{Font.RED}MayDOS/Root/ERROR>>>{e}')
        
def create_dir():
    DIR_LIST = ['MayDOS_Login/', 'important/', 'important/Applications', 'important/log', 'important/download', 'important/download/per.txt']
    for dir in DIR_LIST:
        if dir != DIR_LIST[-1]: 
            if os.path.isdir(dir) == False:
                os.makedirs(dir)
        else:
            if os.path.isdir(dir) == False:
                with open('important/download/per.txt','w') as f:
                    f.write('root')

# 创建更新检测函数
async def check_update_bar(CODE):
    task = asyncio.create_task(check_update(CODE))
    for i in range(1, 101):
        print("\r", end="")
        print("检测更新中: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
    await task    
    
async def check_update(CODE):
    # 读取更新日志
    Update = json.loads(requests.get("https://buelie.github.io/MayDOS/config.json").text)

    # 比较版本号
    if Update["latest"]["default"] != CODE:
        Y_N_U = tkinter.messagebox.askyesno(title='更新提示',message=f'有可用更新，是否下载?\n当前版本: {CODE} -> {Update["latest"]["default"]}\n稍等一下，马上就好，在important/download/找到更新程序并运行即可')
        
        if Y_N_U == True:   # 如果条件为真则执行该线程

            # 检测文件是否存在,如果存在则执行销毁操作
            if os.path.isfile('update.py'):
                os.remove("update.py")
            else:
                pass

            # 下载更新文件并运行
            wget.download("https://buelie.github.io/MayDOS/Update/update.py","")
            os.system("START update.py")
            print("\n")
            
            # 退出线程
            quit()
        else:
            os.system("cls")
    else:
        os.system("cls")

def check_ver():
    try:
        ver_open= open('important/Version.ver', mode='r')
        ver_open.seek(0, 0)
        CODE = ver_open.read()
        return CODE
    except FileNotFoundError:
        print(f'{Font.RED}系统版本文件被移动或异常丢失，请尝试联系我们以修复,可尝试启动OOBE修复{Font.WHITE}')
        input('按下回车键退出. . .')
        quit()
    
def check_user_login():
    try:
        account_open = open('important/account.user',mode='r')
        account_info = account_open.readlines()

        un_username = account_info[0]
        username = un_username[0:-1]

        un_password = account_info[1]
        password = un_password[0:-1]

        account_open.close()
        
        try:
            username = str(base64.b64decode(username),'utf-8')
            password = str(base64.b64decode(password),'utf-8')
        except Exception as e:
            print(f'{Font.RED}ERROR: 账户信息加载失败，账户文件可能损坏，请尝试注销并重新注册{Font.WHITE}')
            print(f'{Font.RED}错误信息：{Font.WHITE}')
            print(e)
            input('按下回车键退出. . .')
            quit()
        
        return account_info, username, password
    
    except FileNotFoundError:
        print(f'{Font.RED}未注册或账户文件异常丢失,可尝试启动OOBE修复{Font.WHITE}')
        input('按下回车键退出. . .')
        quit()

def user_login(account_info, username, password):
    while True:
        match username:
            case "TEST":
                print(account_info)
                print(f'{Font.BLUE}测试账户登录{Font.WHITE}')
                break
            case _:
                print(f'{Font.BEIGE}登录{username}的电脑{Font.WHITE}')
                userspassword = input('密码>')

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
                    f.write(CFILE)
                    f.close()
            #SysPerAPI().cls()
            #os.system('python important/Applications/Notepad/Notepad.py')

    except Exception as e:
        print(f'{Font.RED}MayDOS/Root/ERROR>>>{e}{Font.WHITE}')

def sof(cmd):
    try:
        if cmd.endswith('json'):
            print(f"{Font.RED}MayDOS/Root>>>该文件您无权访问")
        elif cmd.endswith('api') or cmd.endswith('api.py'):
            print(f"{Font.RED}MayDOS/Root>>>该文件您无权访问")
        else:
            if os.path.isfile(f'important/Applications/{cmd[4:-1]}/{cmd[4:-1]}.json') == False or os.path.isfile(f'important/Applications/{cmd[4:-1]}/{cmd[4:-1]}/MAIN.txt') == False:
                match input(f'{Font.YELLOW}MayDos/Root/SOF>>>应用程序"{cmd[4:-1]}"可能已被恶意篡改,请谨慎运行。（Y/N){Font.WHITE}').lower():
                    case "y" | "yes":
                        try:
                            os.system(f'START /MAX "important/Applications/{cmd[4:-1]}/{cmd[4:-1]}.bat"')
                        except Exception as e:
                            print(f'{Font.RED}MayDOS/Root>>>{e}')
                    case 'n' | 'not':
                        pass
                    case _:
                        print("未知操作，已自动退出...")

    except Exception as e:
        print(f'{Font.RED}MayDOS/Root>>>{e}')

def download():
    print("=======================================")
    print("|请选择下载源                         |            \n|1.STORE 默认的应用商店 2.HTTP网络渠道|\n|3.退出                               |")
    print("=======================================")
    match input("MayDOS/download>>>"):
        case '1':
            print("======================================================")
            print("已选择下载源<STORE>,可下载已上传的应用,输入EXIT以退出|")
            print("======================================================")
            while True:
                if input("MayDOS/Download/STORE>>>").lower() == 'exit':
                    break

        case '2': 
            print("=========================================================")
            print("已选择下载源<HTTP>,可下载任何网络上的应用,输入EXIT以退出|")
            print("=========================================================")
            while True:
                D_I_0 = input("MayDOS/Download/STORE>>>")
                if D_I_0.lower() == 'exit':
                    break
                else:
                    wget.download(f'{D_I_0}',"important/download/")

        case _: 
            print("未知操作,已自动退出......")
            print("===================================================")