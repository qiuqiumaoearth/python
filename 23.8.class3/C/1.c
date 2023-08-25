#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 定义员工结构体
struct Employee {
    char emp_id[20];
    char name[50];
    float basic_salary;
    float allowance;
    float bonus;
    float deduction;
};

// 员工数组和员工数量
struct Employee employees[100];
int employeeCount = 0;

// 保存数据到文本文件
void saveDataToFile() {
    FILE* file = fopen("C:\\Users\\HP\\Desktop\\class 3\\职员信息.txt", "a");
    if (file == NULL) {
        printf("无法打开文件。\n");
        return;
    }

    for (int i = 0; i < employeeCount; i++) {
        fprintf(file, "员工号: %s\n", employees[i].emp_id);
        fprintf(file, "姓名: %s\n", employees[i].name);
        fprintf(file, "基本工资: %.2f\n", employees[i].basic_salary);
        fprintf(file, "补贴金额: %.2f\n", employees[i].allowance);
        fprintf(file, "奖励金额: %.2f\n", employees[i].bonus);
        fprintf(file, "扣除金额: %.2f\n", employees[i].deduction);
        fprintf(file, "实发工资: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);
        fprintf(file, "\n");
    }

    fclose(file);
}

// 新增员工
void addEmployee() {
    struct Employee newEmployee;

    printf("请输入员工号: ");
    scanf("%s", newEmployee.emp_id);
    printf("请输入姓名: ");
    scanf("%s", newEmployee.name);
    printf("请输入基本工资: ");
    scanf("%f", &newEmployee.basic_salary);
    printf("请输入补贴金额: ");
    scanf("%f", &newEmployee.allowance);
    printf("请输入奖励金额: ");
    scanf("%f", &newEmployee.bonus);
    printf("请输入扣除金额: ");
    scanf("%f", &newEmployee.deduction);

    employees[employeeCount++] = newEmployee;

    printf("员工信息已保存。\n");
}

// 查找员工
void findEmployee() {
    char empIdToFind[20];
    printf("请输入要查找的员工号: ");
    scanf("%s", empIdToFind);

    for (int i = 0; i < employeeCount; i++) {
        if (strcmp(empIdToFind, employees[i].emp_id) == 0) {
            printf("找到员工信息：\n");
            printf("员工号: %s\n", employees[i].emp_id);
            printf("姓名: %s\n", employees[i].name);
            printf("基本工资: %.2f\n", employees[i].basic_salary);
            printf("补贴金额: %.2f\n", employees[i].allowance);
            printf("奖励金额: %.2f\n", employees[i].bonus);
            printf("扣除金额: %.2f\n", employees[i].deduction);
            printf("实发工资: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);
            return;
        }
    }

    printf("未找到该员工信息。\n");
}

// 删除员工
void deleteEmployee() {
    char empIdToDelete[20];
    printf("请输入要删除的员工号: ");
    scanf("%s", empIdToDelete);

    for (int i = 0; i < employeeCount; i++) {
        if (strcmp(empIdToDelete, employees[i].emp_id) == 0) {
            // 将该员工从数组中移除
            for (int j = i; j < employeeCount - 1; j++) {
                employees[j] = employees[j + 1];
            }
            employeeCount--;
            printf("员工信息已删除。\n");
            return;
        }
    }

    printf("未找到要删除的员工信息。\n");
}

// 修改员工信息
void modifyEmployee() {
    char empIdToModify[20];
    printf("请输入要修改的员工号: ");
    scanf("%s", empIdToModify);

    for (int i = 0; i < employeeCount; i++) {
        if (strcmp(empIdToModify, employees[i].emp_id) == 0) {
            printf("员工原信息如下：\n");
            printf("员工号: %s\n", employees[i].emp_id);
            printf("姓名: %s\n", employees[i].name);
            printf("基本工资: %.2f\n", employees[i].basic_salary);
            printf("补贴金额: %.2f\n", employees[i].allowance);
            printf("奖励金额: %.2f\n", employees[i].bonus);
            printf("扣除金额: %.2f\n", employees[i].deduction);
            printf("实发工资: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);

            printf("请输入新的员工信息：\n");
            printf("请输入姓名: ");
            scanf("%s", employees[i].name);
            printf("请输入基本工资: ");
            scanf("%f", &employees[i].basic_salary);
            printf("请输入补贴金额: ");
            scanf("%f", &employees[i].allowance);
            printf("请输入奖励金额: ");
            scanf("%f", &employees[i].bonus);
            printf("请输入扣除金额: ");
            scanf("%f", &employees[i].deduction);

            printf("员工信息已修改。\n");
            return;
        }
    }

    printf("未找到要修改的员工信息。\n");
}

// 统计员工工资信息
void calculateStatistics() {
    float totalBasicSalary = 0.0;
    float totalAllowance = 0.0;
    float totalBonus = 0.0;
    float totalDeduction = 0.0;
    float totalNetSalary = 0.0;

    for (int i = 0; i < employeeCount; i++) {
        totalBasicSalary += employees[i].basic_salary;
        totalAllowance += employees[i].allowance;
        totalBonus += employees[i].bonus;
        totalDeduction += employees[i].deduction;
        totalNetSalary += employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction;
    }

    printf("所有员工的工资统计信息如下：\n");
    printf("基本工资总额: %.2f\n", totalBasicSalary);
    printf("补贴总额: %.2f\n", totalAllowance);
    printf("奖励总额: %.2f\n", totalBonus);
    printf("扣除总额: %.2f\n", totalDeduction);
    printf("实发工资总额: %.2f\n", totalNetSalary);
    printf("平均实发工资: %.2f\n", totalNetSalary / employeeCount);
}

// 查看所有职员信息
void viewAllEmployees() {
    for (int i = 0; i < employeeCount; i++) {
        printf("员工号: %s\n", employees[i].emp_id);
        printf("姓名: %s\n", employees[i].name);
        printf("基本工资: %.2f\n", employees[i].basic_salary);
        printf("补贴金额: %.2f\n", employees[i].allowance);
        printf("奖励金额: %.2f\n", employees[i].bonus);
        printf("扣除金额: %.2f\n", employees[i].deduction);
        printf("实发工资: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);
        printf("\n");
    }
}

int main() {
    int choice;

    do {
        printf("职工工资管理系统\n");
        printf("1. 新增员工\n");
        printf("2. 查找员工\n");
        printf("3. 删除员工\n");
        printf("4. 修改员工信息\n");
        printf("5. 统计员工工资信息\n");
        printf("6. 查看所有职员信息\n");
        printf("7. 退出\n");
        printf("请选择操作: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addEmployee();
                break;
            case 2:
                findEmployee();
                break;
            case 3:
                deleteEmployee();
                break;
            case 4:
                modifyEmployee();
                break;
            case 5:
                calculateStatistics();
                break;
            case 6:
                viewAllEmployees();
                break;
            case 7:
                // 在程序结束前保存数据到文本文件
                saveDataToFile();
                printf("程序已退出。\n");
                break;
            default:
                printf("无效的选项，请重新选择。\n");
                break;
        }
    } while (choice != 7);

    return 0;
}
