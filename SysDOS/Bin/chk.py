import os

# 获取当前工作目录的路径
current_path = os.getcwd()

# 拼接文件夹路径，这里使用空字符串保持原路径不变
folder_path = current_path + ""

# 检查文件夹路径是否存在
if os.path.exists(folder_path):
    # 如果文件夹存在，则打印确认信息
    print(f"The folder '{folder_path}' exists.")
else:
    # 如果文件夹不存在，则打印相应的信息
    print(f"The folder '{folder_path}' does not exist.")
