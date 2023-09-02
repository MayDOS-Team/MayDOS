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
try:
    import os, sys, asyncio, random
    import important.Applications.MayDOS_Functions as func
    from time import sleep
    #依旧是导库，导不了就安装，Functions的问题仍然没解决（吧）
except Exception as e:
    print(f"{e}\n")
    os.system(r'install.bat')
    os.system(r'cls')
    quit()
    
os.system(r'title MayDOS') # 更改标题

# 环境设置
if os.name == "nt":
    #依旧想改成pass，所以这次我改了
    #os.system("")
    pass
    
# 自动生成/补全 部分文件
func.create_dir()

# 变量设置
Font = func.Font
background = func.Background
SysPerAPI = func.SysPerAPI
with open("important/python_path.txt") as txt:
    PYTHON_PATH: str = txt.readline()
#这个变量真的没问题吗？

CODE = func.check_ver()
#读取版本号

# 以asyncio调用check_update_bar函数
asyncio.run(func.check_update_bar(CODE))

# 打印动画，形式主义
with open("important/icon.txt", "r") as icon:
    for text in icon.readlines():
        print(text)

#读取账户信息（账户名，密码等），详情看MayDOS_Fuctions.py文件
account_info, username, password = func.check_user_login()

    
print(f'{Font.GREEN}欢迎{Font.WHITE}')

#同上
func.user_login(account_info, username, password)

#让用户觉得系统做了很多东西
SysPerAPI().cls()

print(f'{Font.GREEN}正在准备你的MayDOS命令行......{Font.WHITE}')
print(f'{Font.GREEN}请输入"usebook"以打开MayDOS{CODE}的使用手册和帮助{Font.WHITE}')

while True:
    cmd: str = input('MayDOS/Root>>>')
    #下面就是判断用户要干嘛了
    match cmd.lower():
        case "calc":
            os.system(f"{PYTHON_PATH} important/Applications/calc.py")            

        case _ if cmd.lower().startswith("sof"):
            func.sof(cmd)
        
        case _ if cmd.lower().startswith('down'):
            func.download()

        case _ if cmd.lower().startswith('search'):
            search_cmd = r'START https://cn.bing.com/search?q='+cmd[7:]
            try:
                os.popen(search_cmd)
            except Exception as e:
                print("跳转失败")
                print(e)

        case 'usebook' | 'help':
            with open("important/usebook.txt", "r", encoding="utf-8") as menu:
                for text in menu.readlines():
                    print(f"{Font.GREEN}{text}{Font.WHITE}")

        case 'close':
            quit()

        case 'menu':
            #这个是想开发然后没写么？
            pass

        case 'shut':
            #这个可是真的关机
            ans: str = input(f"{Font.RED}确认关机（这可不是闹着玩的）？{Font.WHITE}[Y/N]")
            if ans.lower() == "y":
                if sys.platform == 'win32':
                    os.system('shutdown -p')
                elif sys.platform == 'linux':
                    os.system('shutdown –h now')
                elif sys.platform == 'darwin':
                    os.system('sudo shutdown -h now')
                else:
                    os.system('shutdown -p')
            else:
                break

        case 'notepad':
            func.notepad()

        case 'explorer':
            try:
                SysPerAPI().cls()
                os.system(f'{PYTHON_PATH} important/Applications/Explorer/Explorer.py')
            except:
                print(f'{Font.RED}找不到{cmd}应用程序{Font.WHITE}')

        case 'cls':
            SysPerAPI().cls()
        
        case 'sysver':
            print(f'系统版本：MayDOS {CODE}')
            print('\n开发：MayDOS开发团队 版权所有2023(C)')

        case username:
            List_RAN = ['MayDOS有摸鱼部门和搞事部门！','0.4.1是0.4.2之前最多BUG的版本',
            'MayDOS其实从0.4.0开始就有可安装版本了呢~','MayDOS的安装版本自动更新会报错！',
            'MayDOS现在已经有很多人参与开发了呢','MayDOS的开发人员似乎对MayDOS没有激情',
            'MayDOS的软件API其实和TinOS一样','MayDOS的软件可以无缝移植到TinOS哦!~',
            '其实OOBE中的更新通道仔细一看就感觉不对劲','你知道MayDOS其实在0.4以后有了阁小小的GUI吗？']
            print(f"{Font.YELLOW}未定义的指令，请输入'usebook'以查看使用手册和帮助{Font.WHITE}")
            print("Tips: ", random.choices(List_RAN))

#没了，注释写完了
