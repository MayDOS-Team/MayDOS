def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    print("欢迎使用由MayDOS Team制作的计算器。")
    print("输入'exit'以退出.")
    print("请输入你的表达式:")

    while True:
        expression = input(">>>")

        if expression.lower() == "exit":
            break

        result = calculate(expression)
        print(f"Result: {result}")

main()


# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import messagebox

# ca = tk.Tk()
# ca.title("只因蒜器")
# ca.geometry("305x305")
# ca.minsize(305, 305)
# ca.maxsize(305, 305)
# ca.attributes("-alpha", 0.7)
# ca.configure(bg='#F5F5F5')
# ca["background"] = "#ffffff"

# num = tk.StringVar()
# num.set('')

# f = ("Helvetica", 22)
# f2 = ("Helvetica", 16)
# s = tk.Label(
#     ca,
#     textvariable=num,
#     font=f,
#     height=2,
#     fg='black',
#     bg='white',
#     width=17,
#     justify=tk.LEFT,
#     anchor=tk.SE
# ).grid(row=1, column=1, columnspan=4)

# b_cl = tk.Button(
#     ca,
#     text='C',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='green'
# )

# b_back = tk.Button(
#     ca,
#     text='←',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='gray'
# )

# b_div = tk.Button(
#     ca,
#     text='÷',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='gray'
# )

# b_t = tk.Button(
#     ca,
#     text='x',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='gray'
# )
# b_cl.grid(row=2, column=1, padx=3, pady=2)
# b_back.grid(row=2, column=2, padx=3, pady=2)
# b_div.grid(row=2, column=3, padx=3, pady=2)
# b_t.grid(row=2, column=4, padx=3, pady=2)

# b_7 = tk.Button(
#     ca,
#     text='7',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_8 = tk.Button(
#     ca,
#     text='8',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_9 = tk.Button(
#     ca,
#     text='9',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_mi = tk.Button(
#     ca,
#     text='-',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='gray'
# )

# b_7.grid(row=3, column=1, padx=3, pady=2)
# b_8.grid(row=3, column=2, padx=3, pady=2)
# b_9.grid(row=3, column=3, padx=3, pady=2)
# b_mi.grid(row=3, column=4, padx=3, pady=2)

# b_4 = tk.Button(
#     ca,
#     text='4',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_5 = tk.Button(
#     ca,
#     text='5',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_6 = tk.Button(
#     ca,
#     text='6',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_plus = tk.Button(
#     ca,
#     text='+',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='gray'
# )

# b_4.grid(row=4, column=1, padx=3, pady=2)
# b_5.grid(row=4, column=2, padx=3, pady=2)
# b_6.grid(row=4, column=3, padx=3, pady=2)
# b_plus.grid(row=4, column=4, padx=3, pady=2)

# b_1 = tk.Button(
#     ca,
#     text='1',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_2 = tk.Button(
#     ca,
#     text='2',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_3 = tk.Button(
#     ca,
#     text='3',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_s = tk.Button(
#     ca,
#     text='=',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='gray'
# )

# b_1.grid(row=5, column=1, padx=3, pady=2)
# b_2.grid(row=5, column=2, padx=3, pady=2)
# b_3.grid(row=5, column=3, padx=3, pady=2)
# b_s.grid(row=5, column=4, padx=3, pady=2)

# b_0 = tk.Button(
#     ca,
#     text='0',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_00 = tk.Button(
#     ca,
#     text='00',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_po = tk.Button(
#     ca,
#     text='.',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='white'
# )

# b_up2 = tk.Button(
#     ca,
#     text='x²',
#     width=5,
#     font=f2,
#     relief=tk.FLAT,
#     bg='gray'
# )

# b_0.grid(row=6, column=1, padx=3, pady=2)
# b_00.grid(row=6, column=2, padx=3, pady=2)
# b_po.grid(row=6, column=3, padx=3, pady=2)
# b_up2.grid(row=6, column=4, padx=3, pady=2)


# def cl_b(x):
#     num.set(num.get() + x)


# def con():
#     opt = num.get()
#     if len(opt) >= 1:
#         if opt[len(opt) - 1] == '²':
#             if len(opt) >= 2 and opt[0] != '²':
#                 try:
#                     num.set(int(opt[:len(opt) - 1]) * int(opt[:len(opt) - 1]))
#                 except:
#                     messagebox.showerror('OhShit!!!', '傻逼你不能算符号的平方!!!')
#             else:
#                 messagebox.showerror('OhShit!!!', '傻逼你不能只输入平方!!!')
#         elif opt[len(opt) - 1] not in '1234567890²':
#             messagebox.showerror('OhShit!!!', '傻逼你不能在最后输入符号!!!')
#         elif opt[0] not in '1234567890':
#             messagebox.showerror('OhShit!!!', '傻逼你不能在第一位输入符号!!!')
#         else:
#             try:
#                 re = eval(opt)
#             except ZeroDivisionError:
#                 messagebox.showerror('OhShit!!!', '傻逼你不能除以0!!!')
#             num.set(str(re))
#     else:
#         messagebox.showerror('OhShit!!!', '傻逼你不能不输入数字!!!')


# def cle():
#     num.set('')


# def back():
#     xx = num.get()
#     xx = xx[:-1]
#     num.set(xx)


# def point():
#     num.set(num.get() + '.')

# b_1.config(command = lambda:cl_b('1'))
# b_2.config(command=lambda: cl_b('2'))
# b_3.config(command=lambda: cl_b('3'))
# b_4.config(command=lambda: cl_b('4'))
# b_5.config(command=lambda: cl_b('5'))
# b_6.config(command=lambda: cl_b('6'))
# b_7.config(command=lambda: cl_b('7'))
# b_8.config(command=lambda: cl_b('8'))
# b_9.config(command=lambda: cl_b('9'))
# b_0.config(command=lambda: cl_b('0'))
# b_00.config(command=lambda: cl_b('00'))
# b_plus.config(command=lambda: cl_b('+'))
# b_mi.config(command=lambda: cl_b('-'))
# b_t.config(command=lambda: cl_b('*'))
# b_div.config(command=lambda: cl_b('/'))
# b_up2.config(command=lambda: cl_b('²'))
# b_cl.config(command = cle)
# b_back.config(command = back)
# b_s.config(command = con)
# b_po.config(command=point)


# ca.mainloop()