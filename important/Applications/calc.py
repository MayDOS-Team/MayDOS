import MayDOS_Functions as func

Font = func.Font
background = func.Background
SysPerAPI = func.SysPerAPI

def calculate(expression: str):
    try:
        result: str = eval(expression)
        return result
    except Exception as e:
        print(f"{Font.YELLOW}请输入正确的表达式\nError: {e} {Font.WHITE}")

def save_to_file(result: str):
    with open("../log/calc.log", "a") as file:
        file.write(str(result) + "\n")

def main():
    print("欢迎使用由MayDOS-Team制作的计算器。")
    print("输入\"exit\"以退出.")
    print("请输入你的表达式:")

    while True:
        expression = input(">>>")

        if expression.lower() == "exit":
            break

        result = calculate(expression)
        print(f"Result: {result}")
        save_to_file(result)

main()
