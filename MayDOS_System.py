class Main:
    def main(self):
        # 导入系统相关模块
        import os, sys, random
        # 导入时间模块
        import time
        # 导入自定义系统库
        import SysDOS.Bin.SysLib as syslib

        # 检查并导入第三方库shutil
        if syslib.CheckThirdPartyLib("shutil"):
            import shutil
        else:
            # 如果shutil未安装，则尝试通过pip安装
            os.system("pip3 install shutil")
            import shutil

        # 检查并导入第三方库getpass
        if syslib.CheckThirdPartyLib("getpass"):
            import getpass
        else:
            # 如果getpass未安装，则尝试通过pip安装
            os.system("pip3 install getpass")
            import getpass

        # 检查并导入第三方库base64
        if syslib.CheckThirdPartyLib("base64"):
            pass
        else:
            # 如果base64未安装，则尝试通过pip安装
            os.system("pip3 install base64")

        # 检查并导入第三方库chardet
        if syslib.CheckThirdPartyLib("chardet"):
            import chardet
        else:
            # 如果chardet未安装，则尝试通过pip安装
            os.system("pip3 install chardet")
            import chardet

        os.system(r'title MayDOS')  # 更改标题
        os.system("cls")

        current_path = os.getcwd()

        # 打印动画
        with open(current_path + "\\SysDOS\\Bin\\icon.txt", "r") as icon:
            for text in icon.readlines():
                print(text)

        time.sleep(0.25)
        # 创建系统访问管理器实例，用于后续设置访问类型和用户管理操作
        AccessManager = syslib.SystemAccessManager()
        # 设置系统访问类型为“Normal”，以适应不同的访问控制需求
        AccessManager.SetAccessType("Normal")
        # 列出当前系统中的所有用户名
        UserNameList = syslib.ListUsers()
        # 如果用户列表为空，说明没有用户，因此需要注册一个新用户
        if UserNameList == []:
            syslib.UserRegister()
            # 注册用户后，重新列出系统中的所有用户名
            UserNameList = syslib.ListUsers()
        # 提示用户输入要登录的用户名，用于后续的登录验证
        tmpUserName = input(f"输入要登陆的用户名:")
        # 检查临时用户名是否在用户列表中
        if tmpUserName in UserNameList:
            try:
                # 如果用户名存在，尝试打开对应的用户文件以读取密码
                with open(f"./Users/{tmpUserName}.txt") as f:
                    hashed_user_password = f.read().strip()
                # 验证输入的密码是否与文件中的密码匹配
                if syslib.verify_password(hashed_user_password, getpass.getpass("请输入密码：")):
                    # 密码匹配，登录成功
                    print(f"{syslib.Font.GREEN}登录成功!{syslib.Font.WHITE}")
                    Username = tmpUserName
                else:
                    # 密码不匹配，提示错误并退出程序
                    print(f"{syslib.Font.RED}密码错误{syslib.Style.END}")
                    sys.exit(1)
            except SystemExit:
                # 捕获系统退出异常，确保程序能够正确退出
                exit()
            except:
                # 捕获其他异常，处理损坏的密码情况
                print("损坏的密码")
                quit()
        else:
            # 用户名不存在，提示无效用户并退出程序
            print("无效用户")
            quit()

        os.system("cls")

        # 准备MayDOS命令行环境
        print(f'正在准备你的MayDOS命令行......')
        # 提示用户如何打开使用手册和帮助
        print(f'请输入"usebook"以打开MayDOS的使用手册和帮助')

        # 初始化命令行回显状态
        echo_off = False
        # 初始化命令行提示符
        lx = "$"
        # 初始化当前路径
        path = "~"

        while True:  # 进入命令行循环
            # 根据当前的访问类型（Root或其他用户）以及是否关闭回显来获取用户输入的命令
            if AccessManager.GetAccessType() == "Root":
                # 如果echo_off未启用，则显示特定的提示信息，其中包括路径和用户输入的上一个命令
                if not echo_off:
                    cmd = input(
                        f'{syslib.Font.BEIGE}({syslib.Font.RED}root@MayDOS{syslib.Font.BEIGE})-[{syslib.Font.WHITE}{syslib.Style.BOLD}{path}'
                        f'{syslib.Style.END}'
                        f'{syslib.Font.BEIGE}]'
                        f'{syslib.Font.RED}{lx}{syslib.Font.WHITE}')
                else:
                    # 如果echo_off启用，则不显示任何提示信息，直接获取用户输入
                    cmd = input()
            else:
                # 对于非Root用户，处理方式类似，但提示信息中的用户名和权限级别会有所不同
                if not echo_off:
                    cmd = input(
                        f'{syslib.Font.GREEN}({syslib.Font.BEIGE}{Username}@MayDOS{syslib.Font.GREEN})-[{syslib.Font.WHITE}{path}{syslib.Font.GREEN}]'
                        f'{syslib.Font.BEIGE}{lx}{syslib.Font.WHITE}')
                else:
                    # 如果echo_off启用，则不显示任何提示信息，直接获取用户输入
                    cmd = input()

            match cmd.lower():  # 匹配用户输入的命令
                case _ if cmd.lower().startswith("cat "):  # 如果命令以"cat "开头，则执行文件读取操作
                    path_1 = cmd[4:]  # 获取文件路径
                    try:
                        # 使用chardet检测文件编码
                        encoding = chardet.detect(open(os.path.abspath(path_1), "rb").read())["encoding"]
                        # 打开文件，准备读取内容
                        f = open(os.path.abspath(path_1), "r", encoding=encoding)
                        # 读取文件内容并按行分割
                        content = f.read().split("\n")
                        # 关闭文件
                        f.close()
                        # 遍历文件内容的每一行
                        for i in range(len(content)):
                            # 打印行号和内容
                            print(str(i + 1) + " " + content[i])
                    except Exception as e:
                        # 捕获异常并打印错误信息
                        print(
                            f"{syslib.Font.RED}尝试访问 {syslib.Font.WHITE}{os.path.abspath(path_1)}{syslib.Font.RED} 时报错：{syslib.Font.WHITE}"
                            f"{os.path.abspath(path_1)} {syslib.Font.YELLOW}不是一个有效的文件。{syslib.Font.WHITE}")
                        # 打印具体的异常信息
                        print(e)

                case "sudo su":
                    # 检查访问模式是否为"Normal"，如果是，则尝试提升为"Root"权限
                    if AccessManager.GetAccessType() == "Normal":
                        # 获取用户密码输入，并与存储的密码进行比较
                        if syslib.verify_password(hashed_user_password, getpass.getpass(f"[sudo] {Username}的密码：")):
                            # 密码正确，提升权限并设置路径
                            AccessManager.SetAccessType("Root")
                            path = r"home\MayDOS"
                            lx = "#"
                        else:
                            # 密码错误，显示错误信息
                            print(f"[{syslib.Font.RED}Error{syslib.Font.WHITE}] 密码不正确!")
                    else:
                        # 当前访问模式不是"Normal"，提示用户输入正确的命令以查看使用手册
                        print(
                            f"{syslib.Font.RED}未定义的指令{syslib.Font.YELLOW} sudo su {syslib.Font.RED}，请输入'usebook'以查看使用手册和帮助{syslib.Font.WHITE}")
                # 根据用户选择，展示usebook文本内容
                case 'usebook':
                    # 打开usebook.txt文件，准备读取内容
                    with open(current_path + "\\SysDOS\\Bin\\usebook.txt", "r", encoding="utf-8") as menu:
                        # 逐行读取文件内容并打印
                        for text in menu.readlines():
                            print(text)

                case "calc":
                    # 打开并以二进制模式读取 Python 文件的内容
                    with open(current_path + "\\SysDOS\\AppFile\\calc.py", "rb") as file:
                        # 以UTF-8编码方式解码文件内容
                        calc = file.read().decode('utf-8')

                    # 执行 Python 代码
                    exec(calc)

                case 'notepad':
                    # 询问用户选择命令行还是图形界面来显示记事本
                    dis = input("1.命令行[DOS]\n2.图形界面[GUI]\n请选择显示方式：>>")
                    if dis == '1':
                        # 打开并以二进制模式读取 Python 文件的内容
                        with open(current_path + "\\SysDOS\\AppFile\\Notepad.py", "rb") as file:
                            # 读取的文件内容以UTF-8编码方式解码
                            notepad = file.read().decode('utf-8')

                        # 执行读取的Python代码
                        exec(notepad)


                    elif dis == '2':
                        # 打开并以二进制模式读取 Python 文件的内容
                        with open(current_path + "\\SysDOS\\AppFile\\Notepad_gui.py", "rb") as file:
                            # 以UTF-8编码方式解码文件内容
                            notepad_gui = file.read().decode('utf-8')

                        # 执行 Python 代码
                        exec(notepad_gui)


                    else:
                        print("输入错误，请重新输入")
                        continue

                case 'minesweeper':
                    # 打开并以二进制模式读取 Python 文件的内容
                    with open(current_path + "\\SysDOS\\AppFile\\Minesweeper.py", "rb") as file:
                        # 以UTF-8编码方式解码文件内容
                        minesweeper = file.read().decode('utf-8')

                    # 执行 Python 代码
                    exec(minesweeper)

                # 根据用户输入处理不同的情况
                case 'exit':
                    # 检查当前的访问类型是否为Root
                    if AccessManager.GetAccessType() == "Root":
                        # 如果是Root，则降级访问类型为Normal，并重置相关变量
                        AccessManager.SetAccessType("Normal")
                        lx = "$"
                        path = "~"
                    else:
                        # 如果不是Root，则直接退出程序
                        quit()

                case "reboot":
                    # 清屏然后重新运行
                    os.system("cls")
                    self.main()

                case "user":
                    print("User命令帮助:\n"
                          "user show all            列出当前所有用户以及当前登录用户\n"
                          "user change password     更换当前账户的密码")

                # 根据命令行参数执行相应的用户操作
                case _ if syslib.SplitCommandArguments(cmd.lower(), "one")["Command Name"] == "user":
                    # 获取命令的所有参数，用于后续的具体操作
                    arguments = syslib.SplitCommandArguments(cmd.lower(), "all")["Command Arguments"]
                    # 处理显示所有用户的情况
                    if arguments[0] == "show":
                        if arguments[1] == "all":
                            print('当前系统下可用用户:')
                            for i in syslib.ListUsers():
                                # 根据用户名是否为当前用户，输出不同的提示信息
                                print(i if i != Username else i + "<-当前用户")
                    # 处理更改用户信息的情况
                    elif arguments[0] == "change":
                        # 更改密码的逻辑
                        if arguments[1] == "password":
                            print(f"更改{Username}的密码:")
                            if syslib.verify_password(hashed_user_password, getpass.getpass("输入旧密码")):
                                # 输入并确认新密码
                                PasswordToChange = getpass.getpass("输入新密码")
                                UserPassword = PasswordToChange
                                # 将新密码加密并写入文件
                                hashed_user_password = syslib.hash_password(UserPassword)
                                f = open(os.path.abspath(f"Users\\{Username}.txt"), "w")
                                f.write(hashed_user_password)
                                f.close()
                                print("更改成功!")
                            else:
                                print("更改失败!")
                        # 更改用户名的逻辑
                        elif arguments[1] == "username":
                            print(f"更改{Username}的用户名:")
                            UsernameNew = input("输入新用户名:")
                            # 确保新用户名非空且不存在于系统用户列表中
                            if (UsernameNew != "" or UsernameNew.isspace()) and UsernameNew not in syslib.ListUsers():
                                # 更新用户名，先复制文件再删除原文件
                                open(f"Users/{UsernameNew}.txt", "w").write(open(f"Users/{Username}.txt").read())
                                os.remove(os.path.abspath(f"Users/{Username}.txt"))
                                print(f"{syslib.Font.GREEN}更改成功!{syslib.Font.WHITE}")
                                Username = UsernameNew
                            elif UsernameNew == "" or UsernameNew.isspace():
                                print(f"{syslib.Font.RED}在试图更改用户名时报错:{syslib.Font.YELLOW}用户名为空!{syslib.Font.WHITE}")
                            elif UsernameNew in syslib.ListUsers():
                                print(f"{syslib.Font.RED}在试图更改用户名时报错:{syslib.Font.YELLOW}用户名已存在!{syslib.Font.WHITE}")


                    # 如果操作命令不是前两者，则显示帮助信息
                    else:
                        print("User命令帮助:\n"
                              "user show all            列出当前所有用户以及当前登录用户\n"
                              "user change password     更换当前账户的密码")

                case 'cls':
                    # 典型的清屏
                    os.system('cls')

                case "register" | "reg":
                    # 注册用户
                    syslib.UserRegister()

                # 处理"su"命令，用于切换用户
                case _ if cmd.lower().startswith("su "):
                    # 获取系统中所有的用户名单
                    UserNameList = syslib.ListUsers()
                    if UserNameList != []:
                        # 解析命令行参数，获取目标用户名
                        tmpUserName = syslib.SplitCommandArguments(cmd, "one")["Command Arguments"]
                        if tmpUserName in UserNameList:
                            # 读取目标用户的密码文件
                            with open(os.path.abspath(f"./Users/{tmpUserName}.txt")) as f:
                                TmpUserPassword = f.read()
                            # 循环提示用户输入密码，直到正确
                            while True:
                                pwd = getpass.getpass("输入密码:")
                                if syslib.verify_password(TmpUserPassword, pwd):
                                    # 密码匹配，更新当前用户名和密码
                                    Username = tmpUserName
                                    UserPassword = TmpUserPassword
                                    break
                                else:
                                    # 密码错误，提示用户
                                    print(f"{syslib.Font.RED}密码错误！{syslib.Font.WHITE}")
                        else:
                            # 目标用户不存在，提示用户
                            print(f"{syslib.Font.RED}没有此用户！{syslib.Font.WHITE}")
                    else:
                        # 系统中只有一个用户，提示用户注册新用户
                        print("只有一个用户!\n请使用'register'命令注册用户")

                case 'sysver':
                    print(f'系统版本：MayDOS 1.0.0 Normal')
                    print('开发：MayDOS开发团队 版权所有2023(C)')

                # 添加第三方应用
                # 先判断是否存在ThirdPartyFile文件夹
                # 存在则继续，不存在则创建
                case 'add':
                    if os.path.exists(current_path + "\\SysDOS\\ThirdPartyFile"):
                        print("当前路径存在")

                    else:
                        print("当前路径不存在")
                        os.makedirs(current_path + "\\SysDOS\\ThirdPartyFile")
                        print("已创建路径")

                    # 添加第三方应用，仅限于AddFiles文件夹下的文件，任意文件都可添加，最好为.exe/.txt/.lnk[快捷方式]
                    print("正在检查" + current_path + r"\\AddFiles\\" + "文件夹下是否存在文件...")

                    # 列出AddFiles文件夹下的所有文件，返回一个空列表则为没有文件
                    file_list = os.listdir(current_path + r"\\AddFiles\\")

                    # 判断file_list是否为空列表
                    if file_list == []:
                        print("AddFiles文件夹下没有文件\n请向该目录下添加文件")
                        break
                    else:
                        print("AddFiles文件夹下存在文件\n正在添加文件...")

                    # 列出AddFiles文件夹下的所有文件，将其存入列表内
                    all_file = os.listdir(current_path + r"\\AddFiles\\")

                    # 遍历并复制每个文件到目标目录
                    for file in all_file:
                        # 拼接源文件和目标文件的完整路径
                        source_file = os.path.join(current_path + r"\\AddFiles\\", file)
                        target_file = os.path.join(current_path + r"\\SysDOS\\ThirdPartyFile\\", file)
                        # 复制文件
                        shutil.copy(source_file, target_file)
                        # 输出复制成功，检查目标目录是否存在源文件，不存在则再次复制，否则直接退出
                        if os.path.exists(target_file):
                            print("复制成功")
                        else:
                            print("复制失败，正在重新复制...")
                            shutil.copy(source_file, target_file)
                            print("重新复制成功")
                # 当命令为"ls"时，列出当前目录下的文件
                case _ if cmd.lower() == "ls":
                    try:
                        print(f"当前下的文件：")
                        for i in syslib.ls(os.getcwd()):
                            print(i)
                        print(f"共{len(syslib.ls(os.getcwd()))}个文件。")
                    except FileNotFoundError:
                        print(
                            f"{syslib.Font.RED}尝试访问 {syslib.Font.WHITE}当前目录{syslib.Font.RED} 时报错：{syslib.Font.WHITE}"
                            f"当前目录 {syslib.Font.YELLOW}不是一个有效的文件夹。{syslib.Font.WHITE}")
                # 当命令以"ls "开头时，列出指定目录下的文件
                case _ if cmd.lower().startswith("ls "):
                    tmpcmd = syslib.SplitCommandArguments(cmd, "one")["Command Arguments"]
                    # 检查是否尝试访问系统目录且用户权限非Root，若是，则提示权限不足
                    if os.path.abspath(tmpcmd).startswith(r"C:\Windows") and AccessManager.GetAccessType() != "Root":
                        print(
                            f"{syslib.Font.RED}尝试访问 {syslib.Font.WHITE}{os.path.abspath(tmpcmd)}{syslib.Font.RED} 时报错：{syslib.Font.YELLOW}权限不足。"
                            f"{syslib.Font.WHITE}")
                        continue
                    try:
                        print(f"{os.path.abspath(tmpcmd)}下的文件：")
                        for i in syslib.ls(tmpcmd):
                            print(i)
                        print(f"共{len(syslib.ls(tmpcmd))}个文件。")
                    except FileNotFoundError:
                        print(
                            f"{syslib.Font.RED}尝试访问 {syslib.Font.WHITE}{os.path.abspath(tmpcmd)}{syslib.Font.RED} 时报错：{syslib.Font.WHITE}"
                            f"{os.path.abspath(tmpcmd)} {syslib.Font.YELLOW}不是一个有效的文件夹。{syslib.Font.WHITE}")

                case 'shut':
                    # 真的关机
                    if input(f"确认关机（\x1b[31m这可不是闹着玩的\x1b[0m）？[Y/n]") == "Y":
                        if sys.platform == 'win32':
                            os.system('shutdown -p')

                    else:
                        continue
                case 'fuck':
                    sys.exit(0)

                case _ if cmd.lower().isspace() or cmd.lower() == "":
                    pass

                case _:
                    List_RAN = ['MayDOS有摸鱼部门和搞事部门！', '0.4.1是0.4.2之前最多BUG的版本',
                                'MayDOS其实从0.4.0开始就有可安装版本了呢~', 'MayDOS的安装版本自动更新会报错！',
                                'MayDOS现在已经有很多人参与开发了呢', 'MayDOS的开发人员似乎对MayDOS没有激情',
                                'MayDOS的软件API其实和TinOS一样', 'MayDOS的软件可以无缝移植到TinOS哦!~',
                                '其实OOBE中的更新通道仔细一看就感觉不对劲', '你知道MayDOS其实在0.4以后有了阁小小的GUI吗？',
                                '移除了HIM']
                    print(
                        f"{syslib.Font.RED}未定义的指令{syslib.Font.YELLOW} {cmd} {syslib.Font.RED}，请输入'usebook'以查看使用手册和帮助{syslib.Font.WHITE}")
                    print("Tips: ", random.choice(List_RAN))


Main = Main()
Main.main()
