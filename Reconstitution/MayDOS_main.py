import os
import sys

class Message:
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
            Message(f'The {self.filename} file was read successfully','MayDOS','i').send()
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
File(f'Disk/C/.System/ms_login_user_qx.txt').create(f'3')
File(f'Disk/C/.System/ms_use_help_book.txt').create(f'{use_help}')

class command:
    def __init__(self,command_name:str = '') -> None:
        self.command_name = command_name
        self.command_dict = {
            "help":[3,self.help],
            "sudo":[3,self.sudo]
        }
        return None

    def run(self) -> int:
        try:
            if self.command_name == '':
                pass
            elif self.command_dict.get(self.command_name,400) == 400:
                print(f'[MayDOS | ERROR] $ 命令{self.command_name}不存在')
                return 404
            else:
                with open('Disk/C/.System/ms_login_user_qx.txt','r',encoding='utf-8') as userid:
                    userqx = userid.read()
                if int(userqx) > self.command_dict[self.command_name][0]:
                    print(f'[MayDOS | WARNNING] $ 您的权限不足,无法使用命令{self.command_name}')
                    return 500
                elif int(userqx) <= self.command_dict[self.command_name][0]:
                    command_action = self.command_dict[self.command_name][1]
                    command_action()
                    return 200
        except Exception as error:
            print(f'[MayDOS | ERROR] $ 命令{self.command_name}调用错误')
            print(f'[MayDOS | ERROR] $ {error}')
            return 400

    def help(self):
       with open("Disk/C/.System/ms_use_help_book.txt", "r", encoding="utf-8") as menu:
            for text in menu.readlines():
                sys.stdout.write('')
                print(f"{text}")

    @help
    def usebook(self):
        pass

    def sudo():
        pass

while True:
    command_input = input(f'[MayDOS] $ ')
    command(str(command_input)).run()
