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
