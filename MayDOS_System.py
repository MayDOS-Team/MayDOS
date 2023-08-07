"""
colorama现已弃用

字体样式 -->
Font.BLACK     : 黑色
Font.RED       : 红色
Font.GREEN     : 绿色
Font.YELLOW    : 黄色
Font.BLUE      : 蓝色
Font.VIOLET    :
Font.BEIGE     : 青蓝色
Font.WHITE     : 白色

字体背景样式 -->
Font.BLACK     : 黑色
Font.RED       : 红色
Font.GREEN     : 绿色
Font.YELLOW    : 黄色
Font.BLUE      : 蓝色
Font.VIOLET
Font.WHITE     : 绿色

字体特性/特效 -->
Font.END       : 终端默认设置
Font.BOLD      : 高亮显示
Font.ITALIC    : 斜体文本
Font.URL       : 下划线
Font.BLINK     : 闪烁
Font.BLINK2    : 未知
Font.SELECTED  : 反显

系统颜色表示说明 -->
绿色：提示，正确
红色：警告，错误
黄色：警告，错误（比红色弱一点）
浅蓝色/青蓝色/蓝色：信息，属性
紫红色：暂定
黑色：无（黑色哪看得见？）
"""

import random
import wget
import json
import requests
import os,sys
import time
import base64
import tkinter.messagebox
import asyncio
from time import sleep

os.system(r'title MayDOS') #更改标题

# 环境设置
if os.name == "nt":
    os.system("")
    
"""
自动生成/补全 部分文件
"""
if os.path.isdir('MayDOS_Login/') == False:
    os.makedirs('MayDOS_Login/')
if os.path.isdir('important/') == False:
    os.makedirs('important/')
if os.path.isdir('important/Applications') == False:
    os.makedirs('important/Applications')
if os.path.isdir('important/log') == False:
    os.makedirs('important/log')
if os.path.isdir('important/download') == False:
    os.makedirs('important/download')
if os.path.isfile('important/download/per.txt') == False:
    with open('important/download/per.txt','w') as f:
        f.write('root')
        f.close()

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
                print(f'{Font.YELLOW}Insufficient permissions{Font.WHITE}')
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

# 创建更新检测函数
async def check_update_bar():
    task = asyncio.create_task(check_update())
    for i in range(1, 101):
        print("\r", end="")
        print("检测更新中: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
    await task    
    
async def check_update():
    # 读取更新日志
    Update = json.loads(requests.get("https://buelie.github.io/MayDOS/config.json").text)

    # 当前版本号
    CODE = "0.5.0"

    # 比较版本号
    if Update["latest"]["default"] != CODE:
        Y_N_U = tkinter.messagebox.askyesno(title='更新提示',message=f'有可用更新，是否下载?\n当前版本:{code} -> {Update["latest"]["default"]}\n稍等一下，马上就好，在important/download/找到更新程序并运行即可')
        if Y_N_U == True:
            # 如果条件为真则执行该线程

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
# 变量设置

# 以asyncio调用check_update_bar函数
asyncio.run(check_update_bar())

time_0 = 0.03 # 动画间隔时间

# 打印动画(不要将其存储进文本文件,会读取错误)
print("MMMMMMMM               MMMMMMMM                                             DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS ")
time.sleep(time_0)
print("M:::::::M             M:::::::M                                             D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S")
time.sleep(time_0)
print("M::::::::M           M::::::::M                                             D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S")
time.sleep(time_0)
print("M:::::::::M         M:::::::::M                                             DDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS")
time.sleep(time_0)
print("M::::::::::M       M::::::::::M  aaaaaaaaaaaaayyyyyyy           yyyyyyy       D:::::D    D:::::D O::::::O   O::::::OS:::::S            ")
time.sleep(time_0)
print("M:::::::::::M     M:::::::::::M  a::::::::::::ay:::::y         y:::::y        D:::::D     D:::::DO:::::O     O:::::OS:::::S            ")
time.sleep(time_0)
print("M:::::::M::::M   M::::M:::::::M  aaaaaaaaa:::::ay:::::y       y:::::y         D:::::D     D:::::DO:::::O     O:::::O S::::SSSS         ")
time.sleep(time_0)
print("M::::::M M::::M M::::M M::::::M           a::::a y:::::y     y:::::y          D:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS    ")
time.sleep(time_0)
print("M::::::M  M::::M::::M  M::::::M    aaaaaaa:::::a  y:::::y   y:::::y           D:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS  ")
time.sleep(time_0)
print("M::::::M   M:::::::M   M::::::M  aa::::::::::::a   y:::::y y:::::y            D:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S ")
time.sleep(time_0)
print("M::::::M    M:::::M    M::::::M a::::aaaa::::::a    y:::::y:::::y             D:::::D     D:::::DO:::::O     O:::::O            S:::::S")
time.sleep(time_0)
print("M::::::M     MMMMM     M::::::Ma::::a    a:::::a     y:::::::::y              D:::::D    D:::::D O::::::O   O::::::O            S:::::S")
time.sleep(time_0)
print("M::::::M               M::::::Ma::::a    a:::::a      y:::::::y             DDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S")
time.sleep(time_0)
print("M::::::M               M::::::Ma:::::aaaa::::::a       y:::::y              D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S")
time.sleep(time_0)
print("M::::::M               M::::::M a::::::::::aa:::a     y:::::y               D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS ")
time.sleep(time_0)
print("MMMMMMMM               MMMMMMMM  aaaaaaaaaa  aaaa    y:::::y                DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS   ")
time.sleep(time_0)
print("                                                    y:::::y                                                                            ")
time.sleep(time_0)
print("                                                   y:::::y                                                                             ")
time.sleep(time_0)
print("                                                  y:::::y                                                                              ")
time.sleep(time_0)
print("                                                 y:::::y                                                                               ")
time.sleep(time_0)
print("                                                yyyyyyy                                                                                ")
time.sleep(time_0)
print("================================================================ May DOS V0.5.1 ================================================================")

# 变量设置
error_version_file_not_found = False
error_account_file_not_found = False

try:
    ver_open= open('important/Version.ver',mode='r')
    ver_open.seek(0, 0)
    Ver = ver_open.read()
except  FileNotFoundError:
    error_version_file_not_found = True

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
        print(f'{Font.RED}ERROR_INFOMATION{Font.WHITE}')
        print(e)
        sleep(10)
        quit()
    
except FileNotFoundError:
    error_account_file_not_found = True

if error_account_file_not_found == True and error_version_file_not_found == False:
    print(f'{Font.RED}未注册或账户文件异常丢失,可尝试启动OOBE修复{Font.WHITE}')
    input('按下回车键退出...')
    quit()
elif error_version_file_not_found == True and error_account_file_not_found == False:
    print(f'{Font.RED}系统版本文件被移动或异常丢失，请尝试联系我们以修复,可尝试启动OOBE修复{Font.WHITE}')
    input('按下回车键退出...')
    quit()
elif error_account_file_not_found  and error_version_file_not_found == True:
    print(f'{Font.RED}未找到系统版本文件及账户文件,可尝试启动OOBE修复{Font.WHITE}')
    print(f'{Font.RED}请确认是否注册并尝试联系我们,可尝试启动OOBE修复{Font.WHITE}')
    input('按下回车键退出...')
    quit()
    
if username == 'TEST':
    print(account_info)

print(f'{Font.GREEN}Welcome!')

while True:
    if username == 'TEST':
        print(f'{Font.BLUE}test_account_auto_login{Font.WHITE}')
    else:
        print(f'{Font.BEIGE}登录{username}的电脑{Font.WHITE}')
    
    if username == 'TEST':
        break
    else:
        userspassword = input('密码>')

    if userspassword == password:
        print(f'{Font.GREEN}密码正确')
        break
    else:
        print(f'{Font.RED}密码错误！')
        pass

time.sleep(0.25)
SysPerAPI().cls()

print(f'{Font.GREEN}正在准备你的MayDOS命令行......{Font.WHITE}')
print(f'{Font.GREEN}请输入"usebook"以打开MayDOS0.1的使用手册和帮助{Font.WHITE}')
time.sleep(0.02)

while True:
    cmd = input('MayDOS/Root>>>')
    
    if cmd.lower() == 'calc' :
        os.system('python important/Applications/calc.py')

    elif cmd[0:3].lower() == 'sof':
        try:
            if cmd[4:-1] == 'json':
                print(f"{Font.RED}MayDOS/Root>>>该文件您无权访问")
            elif cmd[4:-1] == 'api' or cmd[4:-1] == 'api.py':
                print(f"{Font.RED}MayDOS/Root>>>该文件您无权访问")
            else:
                if os.path.isfile(f'important/Applications/{cmd[4:-1]}/{cmd[4:-1]}.json') == False or os.path.isfile(f'important/Applications/{cmd[4:-1]}/{cmd[4:-1]}/MAIN.txt') == False:
                    print(f'{Font.YELLOW}MayDos/Root/SOF>>>应用程序"{cmd[4:-1]}"可能已被恶意篡改,请谨慎运行。（Y/N)')
                    Warn_0 = input()
                    if Warn_0 == 'Y' or Warn_0 == 'y' or Warn_0 == 'YES' or Warn_0 == 'yes':
                        try:
                            os.system(f'START /MAX "important/Applications/{cmd[4:-1]}/{cmd[4:-1]}.bat"')
                        except Exception as e:
                            print(f'{Font.RED}MayDOS/Root>>>{e}')
                        except FileNotFoundError as e:
                            print(f'{Font.RED}MayDOS/Root>>>{e}')
                    elif Warn_0 == 'N' or Warn_0 == 'n' or Warn_0 == 'NOT' or Warn_0 == 'not':
                        pass
                    else:
                        print("未知操作，已自动退出...")
        except Exception as e:
            print(f'{Font.RED}MayDOS/Root>>>{e}')

    elif cmd[0:4].lower() = 'down':
        print("=======================================")
        print("|请选择下载源                         |            \n|1.STORE 默认的应用商店 2.HTTP网络渠道|\n|3.退出                               |")
        print("=======================================")
        DOWN_INPUT = input("MayDOS/download>>>")
        if DOWN_INPUT == '1':
            print("======================================================")
            print("已选择下载源<STORE>,可下载已上传的应用,输入EXIT以退出|")
            print("======================================================")
            while True:
                D_I_0 = input("MayDOS/Download/STORE>>>")
                if D_I_0 == 'EXIT' or D_I_0 == 'exit' or D_I_0 == 'Exit':
                    break

        elif DOWN_INPUT == '2': 
            print("=========================================================")
            print("已选择下载源<HTTP>,可下载任何网络上的应用,输入EXIT以退出|")
            print("=========================================================")
            while True:
                D_I_0 = input("MayDOS/Download/STORE>>>")
                if D_I_0.lower() == 'exit':
                    break
                else:
                    wget.download(f'{D_I_0}',"important/download/")

        elif DOWN_INPUT == '3' or DOWN_INPUT == '': 
            pass
        else:
            print("未知操作,已自动退出......")
            print("===================================================")

    elif cmd == "":
        pass

    elif cmd[0:6].lower() == 'search':
        search_cmd = r'START https://cn.bing.com/search?q='+cmd[7:]+'&cvid=aff84598b5bf4a62acc130c33917054f&aqs=edge..69i57j0l3j69i59l2j69i60l3.1183j0j4&FORM=ANAB01&PC=U531'
        try:
            try:
                os.popen(search_cmd)
            except Exception as e:
                os.popen(search_cmd)
                print(" ")
            else:
                print(" ")
        except Exception as e:
            os.popen(search_cmd)
            print(" ")

    elif cmd.lower() == 'usebook'  or cmd.lower() == 'help':
        print(f'{Font.GREEN}SEARCH           互联网搜索')
        print(f'{Font.GREEN}USEBOOK          获取帮助')
        print(f'{Font.GREEN}HELP             获取帮助')
        print(f'{Font.GREEN}MENU             查询程序来源')
        print(f'{Font.GREEN}CALC             打开计算器')
        print(f'{Font.GREEN}CLOSE            退出MayDOS')
        print(f'{Font.GREEN}NOTEPAD          打开记事本程序')
        print(f'{Font.GREEN}EXPLORER         打开资源管理器')
        print(f'{Font.GREEN}CLS              清屏')
        print(f'{Font.GREEN}SYSVER           查看系统版本')
        print(f'{Font.GREEN}DOWN             下载应用程序')
        print(f'{Font.GREEN}SOF <Name>       打开任何应用程序')
        print(f'{Font.BLUE}=====================================')
        print(f'{Font.YELLOW}SHUT             关机(不是闹着玩的！){Font.WHITE}')

    elif cmd.lower() == 'close':
        quit()

    elif cmd.lower() == 'menu':
        pass

    elif cmd.lower() == 'shut':
        if sys.platform == 'win32':
            os.system('shutdown -p')
        elif sys.platform == 'linux':
            os.system('shutdown –h now')
        elif sys.platform == 'darwin':
            os.system('sudo shutdown -h now')
        else:
            os.system('shutdown -p')

    elif cmd.lower() == 'notepad':
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
            Notepad = input('MayDOS/Apply/NOTEPAD>>>')
            if Notepad == 'exit':
                print('\n')
            elif Notepad == '1':
                print(f'模式:正常写入\n')
                CFILE = input("MayDOS/Apply/NOTEPAD/CreatFile>>>")
                with open(CFILE,ENCO_FILE,encoding='utf-8') as f:
                    f.write(CFILE)
                    f.close()
            #SysPerAPI().cls()
            #os.system('python important/Applications/Notepad/Notepad.py')
        except Exception as e:
            print(f'{Font.RED}MayDOS/Root/ERROR>>>{e}{Font.WHITE}')

    elif cmd.lower() == 'explorer':
        try:
            SysPerAPI().cls()
            os.system('python important/Applications/Explorer/Explorer.py')
        except:
            print(f'{Font.RED}找不到{cmd}应用程序{Font.WHITE}')

    elif cmd.lower() == 'cls':
        SysPerAPI().cls()
    elif cmd == username:
        JiTanLaiLuo = 0
        List_RAN = ['MayDOS有摸鱼部门和搞事部门！','0.4.1是0.4.2之前最多BUG的版本',
        'MayDOS其实从0.4.0开始就有可安装版本了呢~','MayDOS的安装版本自动更新会报错！',
        'MayDOS现在已经有很多人参与开发了呢','MayDOS的开发人员似乎对MayDOS没有激情',
        'MayDOS的软件API其实和TinOS一样','MayDOS的软件可以无缝移植到TinOS哦!~',
        '其实OOBE中的更新通道仔细一看就感觉不对劲','你知道MayDOS其实在0.4以后有了阁小小的GUI吗？']
        while True:
            if JiTanLaiLuo != 20 and JiTanLaiLuo < 20:
                tkinter.messagebox.showerror(title="嗨嗨嗨",message="鸡汤来咯!")
                JiTanLaiLuo += 1
            elif JiTanLaiLuo >= 20 and JiTanLaiLuo < 30 :
                tkinter.messagebox.showwarning(title="嗨嗨嗨",message="鸡汤来咯!鸡汤来咯!鸡汤来咯!鸡汤来咯!")
                JiTanLaiLuo += 1
            elif JiTanLaiLuo >= 30:
                tkinter.messagebox.showingo(title="你知道吗?",message=f'{random.choice(List_RAN)}')
                JiTanLaiLuo += 1

    elif cmd.lower() =='sysver':
        print(f'系统版本：MayDOS {Ver}')
        print('\n开发：MayDOS开发团队 版权所有2023(C)')
    else:
        print(f"{Font.YELLOW}未定义的指令，请输入'usebook'以查看使用手册和帮助{Font.WHITE}")
