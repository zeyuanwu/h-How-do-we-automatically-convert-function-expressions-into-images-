import numpy as np
import matplotlib.pyplot as plt
import math

# 安全函数库：只允许这些函数名可用
safe_dict = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'arcsin': np.arcsin,
    'arccos': np.arccos,
    'arctan': np.arctan,
    'log': np.log,
    'log10': np.log10,
    'exp': np.exp,
    'sqrt': np.sqrt,
    'abs': np.abs,
    'sign': np.sign,
    'floor': np.floor,
    'ceil': np.ceil,
    'pi': np.pi,
    'e': np.e,
    'x': None  # 占位符
}

def parse_user_function(expr: str):
    """
    将用户输入的字符串表达式转为可用函数
    例子：expr = 'sin(x) + log(x)'
    """
    def f(x):
        safe_dict['x'] = x
        try:
            return eval(expr, {"__builtins__": {}}, safe_dict)
        except Exception as e:
            print("函数出错：", e)
            return np.nan
    return f

def plot_user_function(expr: str, x_range=(-10, 10)):
    func = parse_user_function(expr)
    x = np.linspace(x_range[0], x_range[1], 400)
    y = func(x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=f"f(x) = {expr}")
    plt.title("用户自定义函数图像")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

# 示例用法
if __name__ == "__main__":
    expr = input("请输入函数表达式，例如 sin(x) + log(x)：\n>>> ")
    plot_user_function(expr)
