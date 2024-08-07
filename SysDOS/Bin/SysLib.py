import os
import time


# 定义一个异常类，用于操作系统开发过程中遇到的错误
class OperationSystemDevelopmentError:
    # 定义一个异常子类，用于处理与命令字符串分割相关的错误
    class SplitPointError:
        # 当尝试分割的点大于要分割的命令字符串长度时抛出此异常
        class SplitPointBiggerThanTheLengthOfTheCommandToSplit(Exception):
            pass

        # 当需要分割但找不到分割点时抛出此异常
        class NeedToSplitButSplitPointNotFoundWhenInvokingTheFunction(Exception):
            pass

        # 当分割点为负数时抛出此异常，因为列表索引不能为负
        class SplitPointIsNegativeButCannotUseIndexThatIsNegativeInAList(Exception):
            pass

    # 定义一个异常子类，用于处理与函数参数相关的错误
    class ArgumentError:
        # 当尝试调用函数时找不到所需参数时抛出此异常
        class ArgumentNotFoundWhenTryingToInvokeTheFunction(Exception):
            pass


def CheckThirdPartyLib(LibNameToImport: str):
    """
    检查第三方库是否已安装。

    该函数尝试导入指定的库，如果导入成功，则表示库已安装，返回True；
    如果导入失败，抛出ImportError异常，则表示库未安装，返回False。

    参数:
    LibNameToImport (str): 需要检查的库的名称。

    返回:
    bool: 如果库已安装，返回True；否则返回False。
    """
    try:
        # 尝试动态导入指定的库
        exec(f"import {LibNameToImport}")
        # 如果导入成功，返回True
        return True
    except ImportError:
        # 如果导入失败，返回False
        return False


if CheckThirdPartyLib("base64"):
    import base64
else:
    os.system("pip install base64")
    import base64


def ListUsers():
    """
    列出Users目录下所有用户的名称。

    本函数通过查看"Users"目录下的文件来获取用户名称列表。
    个用户有一个以".txt"结尾的文件，文件名即为用户名称。

    返回:
        UserNameList: 包含所有用户名称的列表。
    """
    # 初始化一个空列表，用于存储用户名称
    UserNameList = []
    # 遍历"Users"目录下的所有文件和文件夹
    for i in os.listdir(os.path.abspath("./Users")):
        # 检查文件是否以".txt"结尾
        if i.endswith(".txt"):
            # 如果是文本文件，则提取文件名（即用户名称），并将其添加到列表中
            UserNameList.append("".join(i.split(".txt")))
    # 返回包含所有用户名称的列表
    return UserNameList


def UserRegister():
    """
    用户注册函数。
    该函数引导用户通过输入用户名和密码进行注册，如果用户名已存在，则提示用户重新输入用户名。
    如果用户两次输入的密码不一致，则提示用户重新输入密码。当用户名和密码输入完成后，将密码写入以用户名命名的文件中。
    """
    # 循环等待用户输入用户名，直到输入一个不存在的用户名
    while True:
        username = input("注册用户名:")
        # 检查用户名是否已存在于用户列表中
        if username in ListUsers():
            print("用户已存在!")
            continue  # 如果用户名已存在，提示用户重新输入
        userpass = input("密码:")
        # 循环等待用户确认密码，直到两次输入的密码一致
        while True:
            userpass_again = input("再次输入密码:")
            # 检查两次输入的密码是否一致
            if userpass_again != userpass:
                print("密码不正确!")
                # userpass_again = input("再次输入密码:")
                # 上面这sb代码输两次重复密码是吧？
            else:
                # 当密码一致时，将密码写入以用户名命名的文件中，并跳出内层循环
                f = open(os.path.abspath(f"Users\\{username}.txt"), "w")
                f.write(userpass)
                f.close()
                break
        break  # 跳出外层循环，结束注册过程


def SplitCommandArguments(CommandToSplit, CommandSplitType="all", SplitPoint=None):
    """
    分割命令字符串为命令名和参数。

    根据指定的分割类型和分割点，将命令字符串分割为命令名和参数部分。

    参数:
    - CommandToSplit: 待分割的命令字符串。
    - CommandSplitType: 分割类型，可以是"all"、"one"或"Split"。
    - SplitPoint: 分割点，仅在CommandSplitType为"Split"时有效。

    返回:
    - 一个字典，包含"Command Name"（命令名）和"Command Arguments"（命令参数）。

    异常:
    - OperationSystemDevelopmentError.SplitPointError.NeedToSplitButSplitPointNotFoundWhenInvokingTheFunction: 当需要分割但未指定分割点时抛出。
    - OperationSystemDevelopmentError.SplitPointError.SplitPointIsNegativeButCannotUseIndexThatIsNegativeInAList: 当分割点为负数时抛出。
    - OperationSystemDevelopmentError.SplitPointError.SplitPointBiggerThanTheLengthOfTheCommandToSplit: 当分割点大于命令长度时抛出。
    - OperationSystemDevelopmentError.ArgumentError.ArgumentNotFoundWhenTryingToInvokeTheFunction: 当未找到对应的调用方式时抛出。
    """
    # 处理"all"类型分割，返回命令名和全部参数
    if CommandSplitType == "all":
        return {"Command Name": CommandToSplit.split(" ")[0], "Command Arguments": CommandToSplit.split(" ")[1:]}
    # 处理"one"类型分割，返回命令名和连接后的全部参数
    elif CommandSplitType == "one":
        return {"Command Name": CommandToSplit.split(" ")[0],
                "Command Arguments": " ".join(CommandToSplit.split(" ")[1:])}
    # 处理"Split"类型分割，根据指定的分割点分割参数
    elif CommandSplitType == "Split":
        # 如果未指定分割点，则抛出异常
        if SplitPoint == None:
            raise OperationSystemDevelopmentError.SplitPointError.NeedToSplitButSplitPointNotFoundWhenInvokingTheFunction(
                "参数分割点未指定!")
        # 如果分割点为负数，则抛出异常
        elif SplitPoint < 0:
            raise OperationSystemDevelopmentError.SplitPointError.SplitPointIsNegativeButCannotUseIndexThatIsNegativeInAList(
                "参数分割点错误!")
        # 如果分割点大于命令长度，则抛出异常
        elif SplitPoint > len(CommandToSplit.split(" ")):
            raise OperationSystemDevelopmentError.SplitPointError.SplitPointBiggerThanTheLengthOfTheCommandToSplit(
                "参数分割点过大!")
        else:
            out = []
            # 遍历命令字符串的每一部分，找到分割点后进行分割
            for i in range(len(CommandToSplit.split(" "))):
                if i == SplitPoint:
                    one = " ".join(CommandToSplit.split(" ")[i:])
                    two = CommandToSplit.split(" ")[:i]
            # 将分割后的部分添加到结果中
            two.append(one)
            return {"Command Name": CommandToSplit.split(" ")[0], "Command Arguments": two}
    # 如果命令类型无效，则抛出异常
    else:
        raise OperationSystemDevelopmentError.ArgumentError.ArgumentNotFoundWhenTryingToInvokeTheFunction("未找到对应的调用方式!")


class Style:
    """
    定义文本样式的类，包含了一系列文本样式的ASCII控制码。
    这些控制码用于在输出文本时改变其显示样式，比如加粗、斜体等。
    """
    END = '\x1b[0m'  # 重置文本样式的控制码
    BOLD = '\x1b[1m'  # 加粗文本的控制码
    ITALIC = '\x1b[3m'  # 斜体文本的控制码
    UNDERLINE = '\x1b[4m'  # 给文本添加下划线的文本控制码
    BLINK = '\x1b[5m'  # 闪烁效果的文本控制码
    BLINK2 = '\x1b[6m'  # 另一种闪烁效果的文本控制码
    SELECTED = '\x1b[7m'  # 选中状态的文本控制码


class Font:
    """
    定义字体颜色的类，包含了一系列字体颜色的ASCII控制码。
    这些控制码用于在输出文本时改变其字体颜色。
    """
    BLACK = '\x1b[30m'  # 黑色字体的控制码
    RED = '\x1b[31m'  # 红色字体的控制码
    GREEN = '\x1b[32m'  # 绿色字体的控制码
    YELLOW = '\x1b[33m'  # 黄色字体的控制码
    BLUE = '\x1b[34m'  # 蓝色字体的控制码
    VIOLET = '\x1b[35m'  # 紫色字体的控制码
    BEIGE = '\x1b[36m'  # 米色字体的控制码
    WHITE = '\x1b[37m'  # 白色字体的控制码


class Background:
    """
    定义背景颜色的类，包含了一系列背景颜色的ASCII控制码。
    这些控制码用于在输出文本时改变其背景颜色。
    """
    BLACK = '\x1b[40m'  # 黑色背景的控制码
    RED = '\x1b[41m'  # 红色背景的控制码
    GREEN = '\x1b[42m'  # 绿色背景的控制码
    YELLOW = '\x1b[43m'  # 黄色背景的控制码
    BLUE = '\x1b[44m'  # 蓝色背景的控制码
    VIOLET = '\x1b[45m'  # 紫色背景的控制码
    BEIGE = '\x1b[46m'  # 米色背景的控制码
    WHITE = '\x1b[47m'  # 白色背景的控制码


class SystemAccessManager:
    """
    系统访问管理器类，用于管理系统的访问类型。
    """

    def __init__(self):
        """
        初始化系统访问管理器对象。
        """
        # 私有变量，用于存储当前系统的访问类型
        self.__AccessType = ""

    def SetAccessType(self, AccessType: str):
        """
        设置系统的访问类型。

        参数:
        AccessType (str): 指定的访问类型。
        """
        # 将传入的访问类型赋值给内部变量
        self.__AccessType = AccessType

    def GetAccessType(self):
        """
        获取当前系统的访问类型。

        返回:
        当前系统的访问类型字符串。
        """
        # 返回内部存储的访问类型
        return self.__AccessType


def ls(cmd):
    # 验证并获取绝对路径
    abs_path = os.path.abspath(cmd)

    # 检查路径是否存在且为目录
    if not os.path.isdir(abs_path):
        raise ValueError(f"路径 \'{abs_path}\' 不是一个有效目录")

    # 获取目录列表
    directory_list = os.listdir(abs_path)

    # 添加创建时间信息
    creation_time = time.ctime(os.path.getctime(abs_path))
    decorated_list = [f"{item}\t\x1b[32m<{creation_time}>\x1b[0m" for item in directory_list]

    return decorated_list
