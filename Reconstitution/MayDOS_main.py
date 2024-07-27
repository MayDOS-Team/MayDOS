import os
import sys

class Message:

    """
    text:str        输出信息
    applyname:str   输出者
    mode:str        输出模式
    -----------------------
    send     -->    输出函数
    """

    __text:str = 'NULL'
    __mode:str = 'info'
    __applyname:str = 'MayDOS'
    def __init__(self,text:str = __text,applyname:str = __applyname,mode:str = __mode) -> None:
        self.text = text
        self.applyname = applyname
        self.mode = mode
        return None

    def send(self) -> int:
        try:
            if self.mode == 'i':
                print(f'[{self.applyname} | INFO] $ {self.text}')
                return 200
            elif self.mode == 'w':
                print(f'[{self.applyname} | WARNNING] $ {self.text}')
                return 200
            elif self.mode == 'e':
                print(f'[{self.applyname} | ERROR] $ {self.text}')
                return 200
            else:
                print(f'[MayDOS | INFO] $ Error call from {self.applyname}')
                return 400
        except Exception as error:
            print(f'{Fore.RED}[MayDOS | ERROR] $ {error}{Fore.WHITE}')
            return 400

class Folder:

    """
    foldername:str  要处理的文件夹
    ----------------------------
    create    -->   创建函数
    """

    def __init__(self,foldername:str = '') -> None:
        self.foldername = foldername
        return None

    def create(self) -> int:
        try:
            if os.path.isdir(self.foldername) == False:
                os.makedirs(self.foldername)
                Message(f'The {self.foldername} was created successfully','MayDOS','i').send()
                return 200
            else:
                Message(f'Failed to create {self.foldername}','MayDOS','e').send()
                return 400
        except Exception as error:
            Message(f'Failed to create {self.foldername}','MayDOS','e').send()

class File:
    """
    filename:str    要处理的文件
    ----------------------------
    create    -->   创建函数
    writefile -->   写入函数
    readall   -->   读取函数
    """
    def __init__(self,filename:str = 'default.py') -> None:
        self.filename = filename
        return None

    def create(self,text:str = 'NULL',encoding:str = 'utf-8') -> int:
        try:
            if os.path.isfile(self.filename) == False:
                with open(self.filename,'w',encoding=encoding) as newfile:
                    newfile.write(text)
                    newfile.close()
                Message(f'The {self.filename} file was created successfully','MayDOS','i').send()
                return 200
            else:
                Message(f'Failed to create {self.filename}','MayDOS','e').send()
                return 400
        except Exception as error:
            Message(f'Failed to create {self.filename}','MayDOS','e').send()

    def writefile(self,text:str = 'NULL'):
        try:
            with open(self.filename,'w',encoding='utf-8') as writefile:
                writetext = writefile.write(text)
                writefile.close()
            return 200
        except Exception as error:
            Message(f'Failed to write {self.filename}','MayDOS','e').send()
            return 400

    def readall(self,encoding:str = 'utf-8'):
        try:
            with open(self.filename,'r',encoding=encoding) as readfile:
                readtext = readfile.read()
                readfile.close()
            return str(readtext)
        except Exception as error:
            Message(f'Failed to read {self.filename}','MayDOS','e').send()
            return 400

use_help = """
获取更多帮助，请使用"help <command>"或"<command> ?"。
==================================================
SEARCH           互联网搜索
USEBOOK          获取帮助
HELP             获取帮助
MENU             查询程序来源
CALC             打开计算器
CLOSE            退出MayDOS
LS               列出文件夹下的文件
NOTEPAD          打开记事本程序
EXPLORER         打开资源管理器
CLS              清屏
SYSVER           查看系统版本
DOWN             下载应用程序
SOF              打开任何应用程序
==================================================
SHUT             关机(不是闹着玩的！)
"""

Folder(f'Disk').create()
Folder(f'Disk/C').create()
Folder(f'Disk/C/.System').create()
Folder(f'Disk/C/.Help').create()
Folder(f'Disk/C/Users').create()
File(f'Disk/C/.System/ms_login_user_qx.txt').create(f'3')
File(f'Disk/C/.System/ms_use_help_book.txt').create(f'{use_help}')
File(f'Disk/C/.Help/ms_use_help_help.txt').create(f'{use_help}')
File(f'Disk/C/.Help/ms_use_help_usebook.txt').create(f'{use_help}')

class command:
    """
    <command_name>:用户命令

    self.command_name -> 用户命令
    self.command_dict -> 命令字典

    run -> 运行函数
    -----------------------------
    增加命令 :
    【1】 在字典self.command_dict中添加所需命令及参数,注意添加大写命令。

    【2】 在Command类里编写相关函数。

    【3】 字典格式如下:
        "<命令名>":[<权限>,<self.<函数名(不带括号)>]
        * <>为必填项

    【3】 字典参数说明-> <命令名>:字面意思
                      <权限>:  0为系统权限,
                               1为软件权限,
                               2为管理员权限,
                               3为用户权限。
                      <函数名>: 因为运行函数对函数运行做了处理,
                                所以应按照以下格式进行完善填写:
                                <self.<函数名(不带括号)>.

    """

    def __init__(self,command_name:str = '') -> None:
        # 获取用户命令
        self.command_name = command_name

        # 命令存储字典(存入内存,硬编码)
        self.command_dict = {
            "help":[3,self.help],
            "usebook":[3,self.help],
            "cls":[3,self.cls],
            "sudo":[3,self.sudo],
            "HELP":[3,self.help],
            "USEBOOK":[3,self.help],
            "CLS":[3,self.cls],
            "SUDO":[3,self.sudo]
        }

        return None

    def run(self) -> int:
        try:
            # 判断命令是否为空
            if self.command_name == '':
                pass

            # 判断命令是否存在
            elif self.command_dict.get(self.command_name,400) == 400:
                print(f'[MayDOS | ERROR] $ 命令{self.command_name}不存在')
                return 404 # 返回状态码

            # 如果命令存在
            else:
                # 获取当前用户权限
                with open('Disk/C/.System/ms_login_user_qx.txt','r',encoding='utf-8') as userid:
                    userqx = userid.read()

                # 判断权限是否足够
                if int(userqx) > self.command_dict[self.command_name][0]:
                    print(f'[MayDOS | WARNNING] $ 您的权限不足,无法使用命令{self.command_name}')
                    return 500 # 返回状态码

                # 执行命令
                elif int(userqx) <= self.command_dict[self.command_name][0]:
                    command_action = self.command_dict[self.command_name][1]
                    command_action()
                    return 200  # 返回状态码

        except Exception as error:
            print(f'[MayDOS | ERROR] $ 命令{self.command_name}调用错误')
            print(f'[MayDOS | ERROR] $ {error}')
            return 400

    # 注册命令
    def registration(self):
        pass

    # 登录命令
    def login(self):
        pass

    # 帮助命令
    def help(self, command_name:str = 'help'):
        match command_name:
            case 'help' | 'usebook':
                print(f"{File(f'Disk/C/.System/ms_use_help_book.txt').readall()}")
                while True:
                    help_input = input(f'[Help] $ ')
                    match help_input:
                        case 'quit' | 'close' | 'q' | 'c':
                            break
                        case _:
                            try:
                                with open(f'Disk/C/.Help/ms_use_help_{help_input}.txt','r',encoding='utf-8') as help_file:
                                    help_text = help_file.read()
                                    print(f"{help_text}")
                                    help_file.close()
                            except:
                                print(f'[Help] $ 不存在该命令的帮助文件')
            case _:
                print(f'调用错误')
        return 0

    # 清屏命令
    def cls(self):
        os.system(f'cls')

    def sudo():
        pass

class main:
    def __init__(self,**kages) -> None:
        return None

    def run(self) -> None:
        while True:
            command_input = input(f'[MayDOS] $ ')
            command(command_input).run()
        return None

if __name__ == '__main__':
    main().run()
