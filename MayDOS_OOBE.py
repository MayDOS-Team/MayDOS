try:
    import os, json, tkinter as tk, base64
    import important.Applications.MayDOS_Functions as func
    from time import sleep
    #导库，导不了就执行install.bat，然后退出
except Exception as e:
    #弱弱地问一句，是不是还要检查MayDOS_Function.py在不在呢？
    print(f"{e}\n")
    os.system(r'install.bat')
    os.system(r'cls')
    quit()

if os.name == "nt":
    #写pass不香么？鬼知道为什么写这个
    #os.system("")
    pass

# 彩色自定义文本
Font = func.Font    #从MayDOS_Functions.py文件导的
background = func.Background
SysPerAPI = func.SysPerAPI

CODE = func.check_ver()    #读取版本号

#以下为检查文件(夹)的完整性
if not os.path.isdir('MayDOS_Login/'):
    os.makedirs('MayDOS_Login/')
if not os.path.isdir('important/'):
    os.makedirs('important/')
if not os.path.isdir('important/Applications'):
    os.makedirs('important/Applications')
if not os.path.isdir('important/log'):
    os.makedirs('important/log')
if not os.path.isdir('important/download'):
    os.makedirs('important/download')
if not os.path.isfile('important/Version.ver'):
    with open('important/Version.ver','w',encoding='gbk') as f:
        f.write(f"{CODE}\n")
        f.close()
if os.path.isfile('important/download/cg.txt'):
    path_url = os.getcwd() + "\\"
    with open('important/download/cg.txt','w') as f:
        f.write(path_url)
        f.close()
if not os.path.isfile('important/Applications/sys.json'):
    SYS_0 = {"Name":CODE,"description":"MayDOS"}
    with open('important/Applications/sys.json','w') as f:
        SYS_1 = json.dumps(SYS_0,sort_keys=True, indent=4, separators=(',', ':'))
        f.write(SYS_1)
        f.close()
#文件完整性检查到此结束


check_files = os.listdir('important/')
#account_existed = check_files[0]
#上面这个没用的
if 'account.user' in check_files:    #检查账户是否已注册
    print(f'{Font.YELLOW}您已经注册过了{Font.WHITE}')
    input('按任意键退出. . .')
    os.system("START start.bat")
    quit()

def ctd():
    #搞等待的函数，形式主义而已
    for i in range(3, -1, -1):
        print(f'\r下一步...{i}',end='',flush=True)
        sleep(1)

print(f'MayDOS {CODE} OOBE 启动中. . .')
sleep(1)
input('按任意键启动系统')
SysPerAPI().cls()
#清屏

while True:     #设置默认语言
    print('请选择您的默认语言\nPlease choose your default language')
    print('C-Chinese Simplfied（简体中文）')
    lang = input('>').lower()
    if lang == 'c' or lang == 'chinese':
        print(f'已设置默认语言：Chinese Simplfied简体中文')
        ctd()
        break
    else:
        SysPerAPI().cls()
        pass

SysPerAPI().cls()

while True:
    #“友好”地询问用户是否同意
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
        SysPerAPI().cls()
        print('请输入正确的选择！')
        pass

SysPerAPI().cls()
#下面是账户设置，没什么难懂的，就不注释了
print('--------账户设置--------')
username = input('请为您的电脑账户设置一个名称>')
while True :
    password = input('请为您的电脑账户设置一个密码（最好是6位数）>')
    #这里没有重复输密码我是很不认同地，但我就是不想改，反正谁也不会记不住密码，记不住去账户文件复制下来进行base64解码就好了
    if bool(password) == 0 or ' ' in password:
        print("{Font.RED}密码非法，请重试")
    else :
        break

print('账户设置成功！')
print('请确认账户信息：')
print(f'用户名：{username}')
print(f'密码：{password}')
input('按下回车键开始下一步操作...')
SysPerAPI().cls()

print(f'当前版本：{CODE}')
print('请选择是否更新')
#让用户选择更新选项，虽然没什么用，但还是要形式主义一下
while True:
    print('1,自动更新 2,下载更新安装包后让我选择是否安装更新 3,让我选择是否下载并安装更新')
    updatatf_1 = input('>')
    if updatatf_1 == '1':
        updatatf = 'AutoUpdate'
        break
    elif updatatf_1 == '2':
        updatatf = 'DownloadOnly'
        break
    elif updatatf_1 == '3':
        updatatf= 'DoNotUpdate'
        break
    else:
        SysPerAPI().cls()
        print('请输入正确的选项！')
        pass

SysPerAPI().cls()

#这个好像也是形式主义
while True:
    print('请选择更新通道')
    print('A,BetaChannel  B,DevChannel  C,CanaryChannel')
    print('Beta:这些更新由Annie Cathy验证，且比较稳定。此更新通道更新频率为半年一次。适合普通用户使用。')
    print('Dev:这些更新经过Annie Cathy验证，但相较于前一更新通道，此更新通道可能不稳定。此更新通道更新频率为每月一次。适合Windows爱好者使用。')
    print('Canary:此更新不由Annie Cathy验证，且相较于前两个更新通道，此更新通道极不稳定。此更新通道更新频率为每周一次。适合高度技术性用户使用。')
    
    updata_channel = input('>').lower()
    if updata_channel == 'a':
        updatachs = 'Beta_Channel'
        print('你选择了Beta_Channel')
    elif updata_channel == 'b':
        updatachs = 'Dev_Channel'
        print('你选择了DevChannel')
    elif updata_channel == 'c':
        updatachs = 'Canary_Channel'
        print('你选择了CanaryChannel')
    else:
        continue

    with open('important/Version.ver','a',encoding='utf-8') as f:
        f.write(updatachs)
        f.close()
        break

print('更新通道设置完成')

ctd()
SysPerAPI().cls()

print('稍作休息，我们马上就为您准备完成')
#形式主义结束啦！
#下面是对用户名，密码，更新设置和更新路线的内容进行base64编码
b64username = base64.b64encode(username.encode('utf-8'))
b64username = str(b64username,'utf-8')
b64password = base64.b64encode(password.encode('utf-8'))
b64password = str(b64password,'utf-8')
b64updatatf = base64.b64encode(updatatf.encode('utf-8'))
b64updatatf = str(b64updatatf,'utf-8')
b64updatachs = base64.b64encode(updatachs.encode('utf-8'))
b64updatachs = str(b64updatachs,'utf-8')

#然后将编码后的内容写入
account = open('important/account.user',mode='w')
account.write(f'{b64username}\n')
account.write(f'{b64password}\n')
account.write(f'{b64updatatf}\n')
account.write(f'{b64updatachs}')
account.close()
#养成良好习惯，关闭文件，理解成保存也可以

sleep(3)
#形式上的等3秒

print('设置完成！')
print('感谢使用MayDOS！')

ctd()
SysPerAPI().cls()
#下面没有难懂的了
while True:
    print('请选择接下来的操作')
    print(f'1,启动MayDOS 2,退出安装程序')
    lastchs = input('>')
    if lastchs == '1':
        SysPerAPI().cls()
        os.system("START start.bat")
        quit()
    elif lastchs == '2':
        quit()
    else:
        SysPerAPI().cls()
        print('请输入正确的选项！')
        pass
