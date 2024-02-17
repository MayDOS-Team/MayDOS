import os
import datetime
import time
import tkinter as tk
import tkinter.ttk as ttk


# def time_controller_win():
#     pkl = tk.StringVar()
#
#     def add_timer():
#         def setpkl():
#             fun.insert(tk.END, oy.get())
#             win.destroy()
#
#         win = tk.Tk()
#         win.title("Add A New Timer")
#         ttk.Label(win, text="Set The Time").pack()
#         oy = ttk.Entry(win, textvariable=pkl)
#         oy.pack()
#         ttk.Button(win, text="Apply", command=setpkl).pack()
#         win.mainloop()
#
#     def edit_timer():
#         def setpkl():
#             fun.delete(fun.curselection())
#             fun.insert(tk.END, oy.get())
#             win.destroy()
#
#         win = tk.Tk()
#         win.title("Edit The Timer")
#         ttk.Label(win, text="Edit The Timer").pack()
#         oy = ttk.Entry(win, textvariable=pkl)
#         oy.pack()
#         ttk.Button(win, text="Apply", command=setpkl).pack()
#         win.mainloop()
#
#     def apply():
#         result = fun.get(0, 'end')  # 保存所选项为元组
#         s = ' '.join([str(elem) for elem in result])
#         with open("tmp.txt", "w") as tmp:
#             tmp.write(s)
#         timer_o.destroy()
#
#     timer_o = tk.Tk()
#     timer_o.title("Timer")
#     ttk.Button(timer_o, text="+ Add A Timer", command=add_timer).pack()
#     ttk.Button(timer_o, text="Edit The Chosen Timer", command=edit_timer).pack()
#     fun = tk.Listbox(timer_o)
#     fun.pack()
#     ttk.Button(timer_o, text="Apply", command=apply).pack()
#     timer_o.mainloop()
#
#
# time_controller = tk.Tk()
# time_controller.title("Time Terminator Controller")
# menubar = tk.Menu(time_controller)
# time_controller.config(menu=menubar)
#
# operationMenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label="计时器", menu=operationMenu)
# operationMenu.add_cascade()
# operationMenu.add_command(label="计时器", command=time_controller_win)
#
# time_controller.mainloop()

os.system("title Today's Time")


def check(o):
    global a
    now = datetime.datetime.now()
    first = []
    second = []
    third = []
    forth = []
    fifth = []
    sixth = []
    if o == 0:
        a = now.hour
    elif o == 1:
        a = now.minute
        if len(str(a)) != 2:
            a = list(str(a))
            a.insert(0, "0")
            a = "".join(a)
    for k in range(0, 2):
        if str(a)[k] == "0":
            first.insert(1, " 000 ")
            second.insert(1, "0   0")
            third.insert(1, "0   0")
            forth.insert(1, "0   0")
            fifth.insert(1, "0   0")
            sixth.insert(1, " 000 ")
            pass
        if str(a)[k] == "1":
            first.insert(1, "  1  ")
            second.insert(1, " 11  ")
            third.insert(1, "  1  ")
            forth.insert(1, "  1  ")
            fifth.insert(1, "  1  ")
            sixth.insert(1, "11111")
            pass
        if str(a)[k] == "2":
            first.insert(1, " 222 ")
            second.insert(1, "2   2")
            third.insert(1, "   2 ")
            forth.insert(1, " 22  ")
            fifth.insert(1, "2    ")
            sixth.insert(1, "22222")
            pass
        if str(a)[k] == "3":
            first.insert(1, " 333 ")
            second.insert(1, "3   3")
            third.insert(1, "  33 ")
            forth.insert(1, "    3")
            fifth.insert(1, "3   3")
            sixth.insert(1, " 333 ")
            pass
        if str(a)[k] == "4":
            first.insert(1, "   4 ")
            second.insert(1, "  44 ")
            third.insert(1, " 4 4 ")
            forth.insert(1, "4  4 ")
            fifth.insert(1, "44444")
            sixth.insert(1, "   4 ")
            pass
        if str(a)[k] == "5":
            first.insert(1, "55555")
            second.insert(1, "5    ")
            third.insert(1, "5555 ")
            forth.insert(1, "    5")
            fifth.insert(1, "5   5")
            sixth.insert(1, " 555 ")
            pass
        if str(a)[k] == "6":
            first.insert(1, "  6  ")
            second.insert(1, " 6   ")
            third.insert(1, "6    ")
            forth.insert(1, "66666")
            fifth.insert(1, "6   6")
            sixth.insert(1, "66666")
            pass
        if str(a)[k] == "7":
            first.insert(1, "77777")
            second.insert(1, "    7")
            third.insert(1, "   7 ")
            forth.insert(1, "   7 ")
            fifth.insert(1, "  7  ")
            sixth.insert(1, "  7  ")
            pass
        if str(a)[k] == "8":
            first.insert(1, " 888 ")
            second.insert(1, "8   8")
            third.insert(1, " 888 ")
            forth.insert(1, "8   8")
            fifth.insert(1, "8   8")
            sixth.insert(1, " 888 ")
            pass
        if str(a)[k] == "9":
            first.insert(1, "99999")
            second.insert(1, "9   9")
            third.insert(1, "99999")
            forth.insert(1, "    9")
            fifth.insert(1, "   9 ")
            sixth.insert(1, " 99  ")
            pass
        first.insert(1, " ")
        second.insert(1, " ")
        third.insert(1, " ")
        forth.insert(1, " ")
        fifth.insert(1, " ")
        sixth.insert(1, " ")
    # if o == 0:
    #     first.insert(1, "Timer:")
    #     second.insert(1, open("tmp.txt", "r").read())
    print("".join(first))
    print("".join(second))
    print("".join(third))
    print("".join(forth))
    print("".join(fifth))
    print("".join(sixth))


while True:
    bjtime = datetime.datetime.now()
    utc = datetime.datetime.utcnow()
    b = 0
    check(b)
    b = 1
    check(b)
    if len(str(bjtime.hour)) == 1:
        hour = "0" + str(bjtime.hour)
    else:
        hour = bjtime.hour
    if len(str(bjtime.second)) == 1:
        second = "0" + str(bjtime.second)
    else:
        second = str(bjtime.second)
    if len(str(bjtime.minute)) == 1:
        minute = "0" + str(bjtime.minute)
    else:
        minute = str(bjtime.minute)
    if len(str(utc.hour)) == 1:
        utchour = "0" + str(utc.hour)
    else:
        utchour = utc.hour
    if len(str(utc.second)) == 1:
        utcsecond = "0" + str(utc.second)
    else:
        utcsecond = str(utc.second)
    if len(str(utc.minute)) == 1:
        utcminute = "0" + str(utc.minute)
    else:
        utcminute = str(utc.minute)
    print(f"Beijing Time:{bjtime.year}-{bjtime.month}-{bjtime.day} {hour}:{minute}:{second}")
    print(f"UTC Time:{utc.year}-{utc.month}-{utc.day} {utchour}:{utcminute}:{utcsecond}")
    time.sleep(0.1)
    os.system("cls")
