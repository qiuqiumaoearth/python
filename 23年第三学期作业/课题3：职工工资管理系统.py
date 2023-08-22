import tkinter as tk
from tkinter import messagebox

# 定义员工工资数据结构
class Employee:
    def __init__(self, emp_id, name, basic_salary, allowance, bonus, deduction):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.allowance = allowance
        self.bonus = bonus
        self.deduction = deduction
        self.net_salary = basic_salary + allowance + bonus - deduction

# 函数：保存员工信息到文件
def save_employee_data(employee_list, filename):
    with open(filename, 'w') as file:
        for emp in employee_list:
            file.write(f"{emp.emp_id},{emp.name},{emp.basic_salary},{emp.allowance},{emp.bonus},{emp.deduction}\n")

# 函数：加载员工信息文件到内存
def load_employee_data(filename):
    employee_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                emp_data = line.strip().split(',')
                emp = Employee(emp_data[0], emp_data[1], float(emp_data[2]), float(emp_data[3]), float(emp_data[4]), float(emp_data[5]))
                employee_list.append(emp)
    except FileNotFoundError:
        pass
    return employee_list

# 函数：查找员工信息
def find_employee_by_id(employee_list, emp_id):
    for emp in employee_list:
        if emp.emp_id == emp_id:
            return emp
    return None

# 函数：删除员工信息
def delete_employee_by_id(employee_list, emp_id):
    emp = find_employee_by_id(employee_list, emp_id)
    if emp:
        employee_list.remove(emp)
        return True
    return False

# 函数：统计员工工资信息
def calculate_salary_stats(employee_list):
    total_basic_salary = sum(emp.basic_salary for emp in employee_list)
    total_allowance = sum(emp.allowance for emp in employee_list)
    total_bonus = sum(emp.bonus for emp in employee_list)
    total_deduction = sum(emp.deduction for emp in employee_list)
    total_net_salary = sum(emp.net_salary for emp in employee_list)
    average_net_salary = total_net_salary / len(employee_list)

    return {
        'Total Basic Salary': total_basic_salary,
        'Total Allowance': total_allowance,
        'Total Bonus': total_bonus,
        'Total Deduction': total_deduction,
        'Total Net Salary': total_net_salary,
        'Average Net Salary': average_net_salary
    }

# 函数：显示所有员工信息
def display_all_employees():
    info_text.delete(1.0, tk.END)  # 清空文本框内容
    for emp in employees:
        info_text.insert(tk.END, f"员工号: {emp.emp_id}\n")
        info_text.insert(tk.END, f"姓名: {emp.name}\n")
        info_text.insert(tk.END, f"基本工资: {emp.basic_salary}\n")
        info_text.insert(tk.END, f"补贴金额: {emp.allowance}\n")
        info_text.insert(tk.END, f"奖励金额: {emp.bonus}\n")
        info_text.insert(tk.END, f"扣除金额: {emp.deduction}\n")
        info_text.insert(tk.END, f"实发工资: {emp.net_salary}\n\n")

# 函数：新增员工信息
def add_employee():
    emp_id = emp_id_entry.get()
    name = name_entry.get()
    basic_salary = float(basic_salary_entry.get())
    allowance = float(allowance_entry.get())
    bonus = float(bonus_entry.get())
    deduction = float(deduction_entry.get())

    emp = Employee(emp_id, name, basic_salary, allowance, bonus, deduction)
    employees.append(emp)
    save_employee_data(employees, employee_data_file)
    messagebox.showinfo("提示", "员工信息已保存。")

# 函数：查找员工信息
def find_employee():
    emp_id = find_emp_id_entry.get()
    emp = find_employee_by_id(employees, emp_id)
    if emp:
        result_label.config(text=f"姓名: {emp.name}, 实发工资: {emp.net_salary}")
    else:
        result_label.config(text="未找到员工信息。")

# 函数：删除员工信息
def delete_employee():
    emp_id = delete_emp_id_entry.get()
    if delete_employee_by_id(employees, emp_id):
        save_employee_data(employees, employee_data_file)
        messagebox.showinfo("提示", "员工信息已删除。")
    else:
        messagebox.showerror("错误", "未找到员工信息。")

# 创建主窗口
root = tk.Tk()
root.title("职工工资管理系统")

employee_data_file = "employee_data.txt"
employees = load_employee_data(employee_data_file)

# 添加员工界面
add_employee_frame = tk.Frame(root)
add_employee_frame.pack()
tk.Label(add_employee_frame, text="员工号: ").grid(row=0, column=0)
tk.Label(add_employee_frame, text="姓名: ").grid(row=1, column=0)
tk.Label(add_employee_frame, text="基本工资: ").grid(row=2, column=0)
tk.Label(add_employee_frame, text="补贴金额: ").grid(row=3, column=0)
tk.Label(add_employee_frame, text="奖励金额: ").grid(row=4, column=0)
tk.Label(add_employee_frame, text="扣除金额: ").grid(row=5, column=0)

emp_id_entry = tk.Entry(add_employee_frame)
name_entry = tk.Entry(add_employee_frame)
basic_salary_entry = tk.Entry(add_employee_frame)
allowance_entry = tk.Entry(add_employee_frame)
bonus_entry = tk.Entry(add_employee_frame)
deduction_entry = tk.Entry(add_employee_frame)

emp_id_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
basic_salary_entry.grid(row=2, column=1)
allowance_entry.grid(row=3, column=1)
bonus_entry.grid(row=4, column=1)
deduction_entry.grid(row=5, column=1)

add_button = tk.Button(add_employee_frame, text="新增员工", command=add_employee)
add_button.grid(row=6, column=0, columnspan=2)

# 查找员工界面
find_employee_frame = tk.Frame(root)
find_employee_frame.pack()
tk.Label(find_employee_frame, text="查找员工号: ").grid(row=0, column=0)
find_emp_id_entry = tk.Entry(find_employee_frame)
find_emp_id_entry.grid(row=0, column=1)

find_button = tk.Button(find_employee_frame, text="查找员工", command=find_employee)
find_button.grid(row=0, column=2)

result_label = tk.Label(find_employee_frame, text="")
result_label.grid(row=1, column=0, columnspan=3)

# 删除员工信息界面
delete_employee_frame = tk.Frame(root)
delete_employee_frame.pack()
tk.Label(delete_employee_frame, text="删除员工号: ").grid(row=0, column=0)
delete_emp_id_entry = tk.Entry(delete_employee_frame)
delete_emp_id_entry.grid(row=0, column=1)

delete_button = tk.Button(delete_employee_frame, text="删除员工", command=delete_employee)
delete_button.grid(row=0, column=2)

# 查看员工信息按钮
view_button = tk.Button(root, text="查看员工信息", command=display_all_employees)
view_button.pack()

# 创建文本框用于显示员工信息
info_text = tk.Text(root)
info_text.pack()

root.mainloop()
