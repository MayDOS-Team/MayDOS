def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def save_to_file(result):
    with open("important/log/calc.log", "a") as file:
        file.write(str(result) + "\n")

def main():
    print("欢迎使用由Annie_Cathy制作的计算器。")
    print("输入'exit'以退出.")
    print("请输入你的表达式:")

    while True:
        expression = input(">>>")

        if expression.lower() == "exit":
            break

        result = calculate(expression)
        print(f"Result: {result}")
        save_to_file(result)

main()