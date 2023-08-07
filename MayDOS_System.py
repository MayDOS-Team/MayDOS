#colorama使用说明：
#Fore.xxx  前景色（字体颜色）
#Back.xxx 背景色
#Fore常用颜色：
#Fore.GREEN
#Fore.CYAN
#Fore.BLUE
#Fore.RED
#Fore.MAGENTA
#Fore.BLACK
#Fore.YELLOW
#详情请在Py控制台导入colorama并输入help(Fore)
#系统颜色表示说明：
#绿色：提示，正确
#红色：警告，错误
#黄色：警告，错误（比红色弱一点）
#浅蓝色：信息，属性
#紫红色：暂定
#黑色：无（黑色哪看得见？）

import random
import wget
import json
import requests
import os,sys
import time
import base64
from time import sleep
from colorama import Fore, Back, init
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

os.system(r'title MayDOS')
#os.system(r"mode con cols=1280 lines=648")

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

root = tk.Tk()

def show():
    for i in range(100):
        # 每次更新加1
        progressbarOne['value'] = i + 1
        # 更新画面
        root.update()
        time.sleep(0.01)
    Update = json.loads(requests.get("https://buelie.github.io/MayDOS/config.json").text)
    code = "0.4.0"
    if Update["latest"]["default"] != code:
        Y_N_U = tkinter.messagebox.askyesno(title='更新提示',message=f'有可用更新，是否下载?\n当前版本:{code} -> {Update["latest"]["default"]}\n稍等一下，马上就好，在important/download/找到更新程序并运行即可')
        if Y_N_U == True:
            if os.path.isfile('important/download/main.py'):
                os.remove("important/download/main.py")
            else:
                pass
            wget.download("https://buelie.github.io/MayDOS/Update/update.py","")
            os.system("START update.py")
            print("\n")
            quit()
        else:
            root.withdraw()
        root.withdraw()
    else:
        root.withdraw()

Label = ttk.Label(root,text="检查更新中").pack()
progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
progressbarOne['maximum'] = 100
progressbarOne['value'] = 0
progressbarOne['length'] = 200
show()

init(autoreset=True)

time_0 = 0.05

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
print("================================================================ May DOS V0.4.0 ================================================================")

def cls():
    os.system('cls')

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
        print(Fore.RED + 'ERROR: 账户信息加载失败，账户文件可能损坏，请尝试注销并重新注册')
        print(Fore.RED + 'ERROR_INFOMATION')
        print(e)
        sleep(10)
        quit()
    
except FileNotFoundError:
    error_account_file_not_found = True

if error_account_file_not_found == True and error_version_file_not_found == False:
    print(Fore.RED + '未注册或账户文件异常丢失,可尝试启动OOBE修复')
    input('按下回车键退出...')
    quit()
elif error_version_file_not_found == True and error_account_file_not_found == False:
    print(Fore.RED + '系统版本文件被移动或异常丢失，请尝试联系我们以修复,可尝试启动OOBE修复')
    input('按下回车键退出...')
    quit()
elif error_account_file_not_found  and error_version_file_not_found == True:
    print(Fore.RED + '未找到系统版本文件及账户文件,可尝试启动OOBE修复')
    print(Fore.RED + '请确认是否注册并尝试联系我们,可尝试启动OOBE修复')
    input('按下回车键退出...')
    quit()
    
if username == 'TEST':
    print(account_info)

print(Fore.GREEN + 'Welcome!')

while True:
    if username == 'TEST':
        print(Fore.BLUE + 'test_account_auto_login')
    else:
        print(Fore.CYAN + f'登录{username}的电脑')
    
    if username == 'TEST':
        break
    else:
        userspassword = input('密码>')

    if userspassword == password:
        print(Fore.GREEN + '密码正确')
        break
    else:
        print(Fore.RED + '密码错误！')
        pass

sleep(1)
cls()

print(Fore.GREEN + '正在准备你的MayDOS命令行......')
print(Fore.GREEN + '请输入"usebook"以打开MayDOS0.1的使用手册和帮助')
time.sleep(1)

while True:
    cmd = input('MayDOS/Root>>>')
    
    if cmd == 'calc':
        os.system('python important/Applications/calc.py')

    elif cmd[0:3] == 'sof':
        os.system(f'python important/Applications/{cmd[4:-1]}')

    elif cmd == "":
        pass

    elif cmd == 'usebook':
        print(Fore.GREEN + '键入"calc"以打开计算器')
        print(Fore.GREEN + '键入"close"以关闭PyDOS0.1')
        print(Fore.GREEN + '键入"notepad"以打开记事本程序')
        print(Fore.GREEN + '键入"explorer"以打开资源管理器')
        print(Fore.GREEN + '键入"cls"以清屏')
        print(Fore.GREEN + '键入"sysver"以查看系统版本')
        print(Fore.GREEN + '键入"sof <程序名称>"以打开第三方应用程序')

    elif cmd == 'close':
        quit()

    elif cmd == 'notepad':
        try:
            cls()
            os.system('python important/Applications/Notepad.py')
        except:
            print(Fore.RED + f'找不到{cmd}应用程序')

    elif cmd == 'explorer':
        try:
            cls()
            os.system('python important/Applications/Explorer.py')
        except:
            print(Fore.RED + f'找不到{cmd}应用程序')

    elif cmd == 'cls':
        cls()
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

    elif cmd =='sysver':
        print(f'系统版本：MayDOS {Ver}')
        print('\n开发：MayDOS开发团队 版权所有2023(C)')
    else:
        print(Fore.YELLOW + "未定义的指令",cmd,Fore.YELLOW + "，请输入'usebook'以查看使用手册和帮助")

root.mainloop()