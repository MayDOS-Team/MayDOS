import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import base64
import os

current_path = os.path.abspath(os.getcwd())

messagebox.showinfo("使用说明", "Notepad_GUI 0.1\n保存文件时需要手动输入文件扩展名，此漏洞将在下一个版本修复！")

ver = "Notepad_GUI 0.1"
info = "\n当前功能暂未实现。\n但是你可以在Bilibili上关注Minecraft_2v以了解更新进度。\n或添加作者QQ：2306925195以了解更新进度。"


def version():
    messagebox.showinfo("关于", "Notepad_GUI 0.1\n作者：MayDOS Team")


def use_book():
    messagebox.showinfo("使用说明", "Notepad_GUI 0.1\n保存文件时需要手动输入文件扩展名，此漏洞将在下一个版本修复！")


def new_file():
    text.delete("1.0", tk.END)
    root.title("Notepad_GUI")


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("MayDOS专有格式", "*.MayNote"), ("文本文档", "*.txt"), ("全部文件", "*.*")])
    if file_path:
        try:
            if file_path.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as file:
                    text.delete("1.0", tk.END)
                    text.insert("1.0", file.read())
                    root.title(f"Notepad_GUI - {file_path}")
            elif file_path.endswith(".MayNote"):
                with open(file_path, "r", encoding="utf-8") as file:
                    encoded_content = file.read()
                    decoded_content = base64.b64decode(encoded_content).decode("utf-8")
                    text.delete("1.0", tk.END)
                    text.insert("1.0", decoded_content)
                    root.title(f"Notepad_GUI - {file_path}")
        except Exception as e:
            messagebox.showerror("打开文件错误", f"无法打开文件：{str(e)}")


def save_file():
    file_path = filedialog.asksaveasfilename(
        filetypes=[("MayDOS专有格式", "*.MayNote"), ("文本文档", "*.txt"), ("全部文件", "*.*")])
    if file_path:
        try:
            if file_path.endswith(".txt"):
                if not file_path.endswith(".txt"):
                    file_path += ".txt"
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text.get("1.0", tk.END))
                    root.title(f"Notepad_GUI - {file_path}")
            elif file_path.endswith(".MayNote"):
                encoded_content = base64.b64encode(text.get("1.0", tk.END).encode("utf-8")).decode("utf-8")
                if not file_path.endswith(".MayNote"):
                    file_path += ".MayNote"
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(encoded_content)
                    root.title(f"Notepad_GUI - {file_path}")
        except Exception as e:
            messagebox.showerror("保存文件错误", f"无法保存文件：{str(e)}")


def cut():
    text.event_generate("<<Cut>>")


def copy():
    text.event_generate("<<Copy>>")


def paste():
    text.event_generate("<<Paste>>")


def undo():
    try:
        text.edit_undo()
    except tk.TclError:
        pass


def redo():
    try:
        text.edit_redo()
    except tk.TclError:
        pass


def check_update():
    messagebox.showinfo("检查更新", "当前版本为：" + ver + info)


def open_url():
    webbrowser.open("https://space.bilibili.com/3493262897711201")
    messagebox.showinfo("关注作者", "已经打开Bilibili并关注该作者")


def team_member_command():
    team_member = ['姗姗来迟的晚霞',
                   '是螺螺呀',
                   '图佟15',
                   '小严awa',
                   '御坂10032号',
                   '账号已封禁',
                   'bil_fis',
                   'Jincheng(BUID:3493124978510331)',
                   'creeper',
                   'HOW ARE YOU',
                   'kddddddde',
                   '苦麒麟kuqilin',
                   '乐乐',
                   'Mr_xiaoliu',
                   'rRichard',
                   '有点坏儿bitbad']

    messagebox.showinfo("Note", "此名字均为QQ昵称。\n此显示顺序没有特殊排序，遵循QQ上显示的顺序")

    for mem in team_member:
        messagebox.showinfo("团队成员", "我们的团队成员有：" + mem)


root = tk.Tk()
root.title("Notepad_GUI")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(label="新建", command=new_file)
file_menu.add_command(label="打开", command=open_file)
file_menu.add_command(label="保存", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="编辑", menu=edit_menu)
edit_menu.add_command(label="剪切", command=cut)
edit_menu.add_command(label="复制", command=copy)
edit_menu.add_command(label="粘贴", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="撤销", command=undo)
edit_menu.add_command(label="重做", command=redo)

program_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="应用程序", menu=program_menu)
program_menu.add_command(label="Help/使用提示", command=use_book)
program_menu.add_separator()
program_menu.add_command(label="检查更新", command=check_update)
program_menu.add_separator()
program_menu.add_command(label="在Bilibili上关注作者", command=open_url)
program_menu.add_separator()
program_menu.add_command(label="关于", command=version)

team_member_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="开发者", menu=team_member_menu)
team_member_menu.add_command(label="关于团队", command=team_member_command)

root.mainloop()
