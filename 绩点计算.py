import sys
import subprocess

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    # 尝试导入 kivy
    import kivy
except ImportError:
    print("正在安装 kivy。")
    install_package("kivy")

# Tkinter 程序部分
import tkinter as tk
from tkinter import messagebox

def add_course():
    try:
        grade = float(grade_entry.get())
        credit = float(credit_entry.get())
        course = course_entry.get()
        courses.append((grade, credit, course))
        grade_entry.delete(0, tk.END)
        credit_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        course_list_var.set(course_list_var.get() + f"{course}: 绩点={grade}, 学分={credit}\n")
    except ValueError:
        messagebox.showerror("输入错误", "请确保绩点是数字")

def calculate_gpa():
    total_points = 0
    total_credits = 0
    for grade, credit, _ in courses:
        total_points += grade * credit
        total_credits += credit
    if total_credits > 0:
        average_gpa = total_points / total_credits
        messagebox.showinfo("平均学分绩点", f"平均学分绩点是: {average_gpa:.4f}")
    else:
        messagebox.showerror("计算错误", "无法计算平均学分绩点, 因为总学分为0")

# 初始化 Tkinter 窗口
root = tk.Tk()
root.title("学分绩点计算器")

# 创建变量来存储输入的数据
courses = []

# 创建输入框和标签
tk.Label(root, text="绩点").grid(row=0, column=0)
grade_entry = tk.Entry(root)
grade_entry.grid(row=0, column=1)

tk.Label(root, text="学分").grid(row=1, column=0)
credit_entry = tk.Entry(root)
credit_entry.grid(row=1, column=1)

tk.Label(root, text="课程名称").grid(row=2, column=0)
course_entry = tk.Entry(root)
course_entry.grid(row=2, column=1)

# 创建按钮
add_button = tk.Button(root, text="添加", command=add_course)
add_button.grid(row=3, column=0)

calculate_button = tk.Button(root, text="计算平均学分绩点", command=calculate_gpa)
calculate_button.grid(row=3, column=1)

# 创建一个文本区域以显示已添加的课程
course_list_var = tk.StringVar()
course_list_label = tk.Label(root, textvariable=course_list_var, justify=tk.LEFT)
course_list_label.grid(row=4, column=0, columnspan=2)

# 运行主循环
root.mainloop()




