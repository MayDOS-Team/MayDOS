import os
import time
import base64
import json
import tkinter as tk
from time import sleep

if os.name == "nt":
    os.system("")

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

try:
    readversion = open('important/Version.ver',mode='r')
    readversion.seek(0, 0)
    version = readversion.read()
    readversion.close()
except FileNotFoundError:
    print(f'{Font.RED}ERROR：无法找到文件Version.ver{Font.WHITE}')
    input('按任意键退出. . .')
    quit()

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
if os.path.isfile('important/Version.ver') == False:
    with open('important/Version.ver','w',encoding='gbk') as f:
        f.write(f"{version}\n")
        f.close()
if os.path.isfile('important/download/cg.txt') == False:
    path_url = os.getcwd() + "\\"
    with open('important/download/cg.txt','w') as f:
        f.write(path_url)
        f.close()
if os.path.isfile('important/Applications/sys.json') == False:
    SYS_0 = {"Name":version,"description":"a cui dos"}
    with open('important/Applications/sys.json','w') as f:
        SYS_1 = json.dumps(SYS_0,sort_keys=True, indent=4, separators=(',', ':'))
        f.write(SYS_1)
        f.close()


tk = tk.Tk()

tk.withdraw()

check_files = os.listdir('important/')
account_existed = check_files[0]
if account_existed == 'account.user':
    print(f'{Font.YELLOW}您已经注册过了{Font.WHITE}')
    input('按任意键退出. . .')
    os.system("START start.bat")
    quit()

def cls():
    os.system('cls')

def ctd():
    for i in range(3):
        list = ['3','2','1','0']
        index = i % 4
        print('\r下一步...{}'.format(list[index]),end='',flush=True)
        sleep(1)

print(f'MayDOS {version} OOBE 启动中. . .')
sleep(2)
input('按任意键启动系统')
cls()

while True:     #Default Language Set
    print('请选择您的默认语言\nPlease choose your default language')
    print('C-Chinese Simplfied（简体中文）')
    lang = input('>').lower()
    if lang == 'C' or lang == 'chinese':
        print(f'已设置默认语言：Chinese Simplfied简体中文')
        ctd()
        break
    else:
        cls()
        pass

cls()

while True:
    print('欢迎使用MayDOS！')
    print('请查看此协议条款并进行下一步安装')
    print('This system made by Annie Cathy.Copyright 2023 (R).This Program is free for use!')
    print('Y 同意并继续  N 拒绝并退出')
    aoachk = input('[Y/N]...').lower()
    if aoachk == 'y':
        print('您已同意此协议条款')
        ctd()
        break
    elif aoachk == 'n':
        print('您拒绝了此协议条款')
        print('即将退出')
        ctd()
        quit()
    else:
        cls()
        print('请输入正确的选择！')
        pass

cls()

print('--------账户设置--------')
username = input('请为您的电脑账户设置一个名称>')
while True :
    password = input('请为您的电脑账户设置一个密码（最好是6位数）>')
    if bool(password) == 0 or ' ' in password:
        print("{Font.RED}密码非法，请重试")
    else :
        break
print('账户设置成功！')
print('请确认账户信息：')
print(f'用户名：{username}')
print(f'密码：{password}')
input('按下回车键开始下一步操作...')
cls()

print(f'当前版本：{version}')
print('请选择是否更新')
while True:
    print('1,自动更新 2,下载更新安装包后让我选择是否安装更新 3,让我选择是否下载并安装更新')
    updatatf_1 = input('>')
    if updatatf_1 == '1':
        updatatf = 'AutoUpdata'
        break
    elif updatatf_1 == '2':
        updatatf = 'DownloadOnly'
        break
    elif updatatf_1 == '3':
        updatatf= 'DoNotUpdate'
        break
    else:
        cls()
        print('请输入正确的选项！')
        pass

cls()

while True:
    print('请选择更新通道')
    print('A,BetaChannel  B,DevChannel  C,CanaryChannel')
    print('Beta:这些更新由Annie Cathy验证，且比较稳定。此更新通道更新频率为半年一次。适合普通用户使用。')
    print('Dev:这些更新经过Annie Cathy验证，但相较于前一更新通道，此更新通道可能不稳定。此更新通道更新频率为每月一次。适合Windows爱好者使用。')
    print('Canary:此更新不由Annie Cathy验证，且相较于前两个更新通道，此更新通道极不稳定。此更新通道更新频率为每周一次。适合高度技术性用户使用。')
    updata_channel = input('>')
    if updata_channel == 'A' or updata_channel == 'a':
        updatachs = 'Beta_Channel'
        print('你选择了Beta_Channel')
        with open('important/Version.ver','a',encoding='utf-8') as f:
            f.write("Dev_Channel")
            f.close()
        break
    elif  updata_channel == 'B' or updata_channel == 'b':
        updatachs = 'Dev_Channel'
        print('你选择了DevChannel')
        with open('important/Version.ver','a',encoding='utf-8') as f:
            f.write("Dev_Channel")
            f.close()
        break
    elif updata_channel == 'C' or updata_channel == 'c':
        updatachs = 'Canary_Channel'
        print('你选择了CanaryChannel')
        with open('important/Version.ver','a',encoding='utf-8') as f:
            f.write("Canary_Channel")
            f.close()
        break

print('更新通道设置完成')

ctd()
cls()

print('稍作休息，我们马上就为您准备完成')

b64username = base64.b64encode(username.encode('utf-8'))
b64username = str(b64username,'utf-8')
b64password = base64.b64encode(password.encode('utf-8'))
b64password = str(b64password,'utf-8')
b64updatatf = base64.b64encode(updatatf.encode('utf-8'))
b64updatatf = str(b64updatatf,'utf-8')
b64updatachs = base64.b64encode(updatachs.encode('utf-8'))
b64updatachs = str(b64updatachs,'utf-8')

account = open('important/account.user',mode='w')
account.write(f'{b64username}\n')
account.write(f'{b64password}\n')
account.write(f'{b64updatatf}\n')
account.write(f'{b64updatachs}')
account.close()

sleep(5)

print('设置完成！')
print('感谢使用MayDOS！')

ctd()
cls()

while True:
    print('请选择接下来的操作')
    print(f'1,启动MayDOS 2,退出安装程序')
    lastchs = input('>')
    if lastchs == '1':
        cls()
        os.system("START start.bat")
        quit()
    elif lastchs ==  '2':
        quit()
    else:
        cls()
        print('请输入正确的选项！')
        pass

tk.mainloop()