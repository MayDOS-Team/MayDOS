import os
import time
import base64
from time import sleep
from colorama import Fore, init

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
        f.write("V0.4.2 内测版\n")
        f.close()
if os.path.isfile('important/download/cg.txt') == False:
    path_url = os.getcwd() + "\\"
    with open('important/download/cg.txt','w') as f:
        f.write(path_url)
        f.close()

init(autoreset=True)

check_files = os.listdir('important/')
account_existed = check_files[0]
if account_existed == 'account.user':
    print(Fore.YELLOW + 'You have already registered')
    input('Press Enter to close...')
    os.system("START start.bat")
    quit()

try:
    readversion = open('important/Version.ver',mode='r')
    readversion.seek(0, 0)
    version = readversion.read()
    readversion.close()
except FileNotFoundError:
    print(Fore.RED + 'ERROR_Version_File_Not_Found')
    input('Press Enter to close...')
    quit()

def cls():
    os.system('cls')

def ctd():
    for i in range(3):
        list = ['3','2','1','0']
        index = i % 4
        print('\r下一步...{}'.format(list[index]),end='',flush=True)
        sleep(1)

print(f'MayDOS {version} OOBE starting up...')
sleep(2)
input('Press Enter to setup your system')
cls()

while True:     #Default Language Set
    print('Please choose your default language')
    print('C-Simple Chinese')
    lang = input('>')
    if lang == 'C' or lang == 'c' or lang == 'chinese' or lang == 'Chinese':
        print(f'已设置默认语言：Simple Chinese简体中文')
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
    aoachk = input('[Y/N]...')
    if aoachk == 'y' or aoachk == 'Y':
        print('您已同意此协议条款')
        ctd()
        break
    elif aoachk == 'n' or aoachk == 'N':
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
password = input('请为您的电脑账户设置一个密码（最好是6位数）>')
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
        updatatf= 'DoNotUpdata'
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
        updatachs = 'BetaChannel'
        print('你选择了BetaChannel')
        with open('important/Version.ver','a',encoding='utf-8') as f:
            f.write("DevChannel")
            f.close()
        break
    elif  updata_channel == 'B' or updata_channel == 'b':
        updatachs = 'DevChannel'
        print('你选择了DevChannel')
        with open('important/Version.ver','a',encoding='utf-8') as f:
            f.write("DevChannel")
            f.close()
        break
    elif updata_channel == 'C' or updata_channel == 'c':
        updatachs = 'CanaryChannel'
        print('你选择了CanaryChannel')
        with open('important/Version.ver','a',encoding='utf-8') as f:
            f.write("CanaryChannel")
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
