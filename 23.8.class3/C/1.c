#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ����Ա���ṹ��
struct Employee {
    char emp_id[20];
    char name[50];
    float basic_salary;
    float allowance;
    float bonus;
    float deduction;
};

// Ա�������Ա������
struct Employee employees[100];
int employeeCount = 0;

// �������ݵ��ı��ļ�
void saveDataToFile() {
    FILE* file = fopen("C:\\Users\\HP\\Desktop\\class 3\\ְԱ��Ϣ.txt", "a");
    if (file == NULL) {
        printf("�޷����ļ���\n");
        return;
    }

    for (int i = 0; i < employeeCount; i++) {
        fprintf(file, "Ա����: %s\n", employees[i].emp_id);
        fprintf(file, "����: %s\n", employees[i].name);
        fprintf(file, "��������: %.2f\n", employees[i].basic_salary);
        fprintf(file, "�������: %.2f\n", employees[i].allowance);
        fprintf(file, "�������: %.2f\n", employees[i].bonus);
        fprintf(file, "�۳����: %.2f\n", employees[i].deduction);
        fprintf(file, "ʵ������: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);
        fprintf(file, "\n");
    }

    fclose(file);
}

// ����Ա��
void addEmployee() {
    struct Employee newEmployee;

    printf("������Ա����: ");
    scanf("%s", newEmployee.emp_id);
    printf("����������: ");
    scanf("%s", newEmployee.name);
    printf("�������������: ");
    scanf("%f", &newEmployee.basic_salary);
    printf("�����벹�����: ");
    scanf("%f", &newEmployee.allowance);
    printf("�����뽱�����: ");
    scanf("%f", &newEmployee.bonus);
    printf("������۳����: ");
    scanf("%f", &newEmployee.deduction);

    employees[employeeCount++] = newEmployee;

    printf("Ա����Ϣ�ѱ��档\n");
}

// ����Ա��
void findEmployee() {
    char empIdToFind[20];
    printf("������Ҫ���ҵ�Ա����: ");
    scanf("%s", empIdToFind);

    for (int i = 0; i < employeeCount; i++) {
        if (strcmp(empIdToFind, employees[i].emp_id) == 0) {
            printf("�ҵ�Ա����Ϣ��\n");
            printf("Ա����: %s\n", employees[i].emp_id);
            printf("����: %s\n", employees[i].name);
            printf("��������: %.2f\n", employees[i].basic_salary);
            printf("�������: %.2f\n", employees[i].allowance);
            printf("�������: %.2f\n", employees[i].bonus);
            printf("�۳����: %.2f\n", employees[i].deduction);
            printf("ʵ������: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);
            return;
        }
    }

    printf("δ�ҵ���Ա����Ϣ��\n");
}

// ɾ��Ա��
void deleteEmployee() {
    char empIdToDelete[20];
    printf("������Ҫɾ����Ա����: ");
    scanf("%s", empIdToDelete);

    for (int i = 0; i < employeeCount; i++) {
        if (strcmp(empIdToDelete, employees[i].emp_id) == 0) {
            // ����Ա�����������Ƴ�
            for (int j = i; j < employeeCount - 1; j++) {
                employees[j] = employees[j + 1];
            }
            employeeCount--;
            printf("Ա����Ϣ��ɾ����\n");
            return;
        }
    }

    printf("δ�ҵ�Ҫɾ����Ա����Ϣ��\n");
}

// �޸�Ա����Ϣ
void modifyEmployee() {
    char empIdToModify[20];
    printf("������Ҫ�޸ĵ�Ա����: ");
    scanf("%s", empIdToModify);

    for (int i = 0; i < employeeCount; i++) {
        if (strcmp(empIdToModify, employees[i].emp_id) == 0) {
            printf("Ա��ԭ��Ϣ���£�\n");
            printf("Ա����: %s\n", employees[i].emp_id);
            printf("����: %s\n", employees[i].name);
            printf("��������: %.2f\n", employees[i].basic_salary);
            printf("�������: %.2f\n", employees[i].allowance);
            printf("�������: %.2f\n", employees[i].bonus);
            printf("�۳����: %.2f\n", employees[i].deduction);
            printf("ʵ������: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);

            printf("�������µ�Ա����Ϣ��\n");
            printf("����������: ");
            scanf("%s", employees[i].name);
            printf("�������������: ");
            scanf("%f", &employees[i].basic_salary);
            printf("�����벹�����: ");
            scanf("%f", &employees[i].allowance);
            printf("�����뽱�����: ");
            scanf("%f", &employees[i].bonus);
            printf("������۳����: ");
            scanf("%f", &employees[i].deduction);

            printf("Ա����Ϣ���޸ġ�\n");
            return;
        }
    }

    printf("δ�ҵ�Ҫ�޸ĵ�Ա����Ϣ��\n");
}

// ͳ��Ա��������Ϣ
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

    printf("����Ա���Ĺ���ͳ����Ϣ���£�\n");
    printf("���������ܶ�: %.2f\n", totalBasicSalary);
    printf("�����ܶ�: %.2f\n", totalAllowance);
    printf("�����ܶ�: %.2f\n", totalBonus);
    printf("�۳��ܶ�: %.2f\n", totalDeduction);
    printf("ʵ�������ܶ�: %.2f\n", totalNetSalary);
    printf("ƽ��ʵ������: %.2f\n", totalNetSalary / employeeCount);
}

// �鿴����ְԱ��Ϣ
void viewAllEmployees() {
    for (int i = 0; i < employeeCount; i++) {
        printf("Ա����: %s\n", employees[i].emp_id);
        printf("����: %s\n", employees[i].name);
        printf("��������: %.2f\n", employees[i].basic_salary);
        printf("�������: %.2f\n", employees[i].allowance);
        printf("�������: %.2f\n", employees[i].bonus);
        printf("�۳����: %.2f\n", employees[i].deduction);
        printf("ʵ������: %.2f\n", employees[i].basic_salary + employees[i].allowance + employees[i].bonus - employees[i].deduction);
        printf("\n");
    }
}

int main() {
    int choice;

    do {
        printf("ְ�����ʹ���ϵͳ\n");
        printf("1. ����Ա��\n");
        printf("2. ����Ա��\n");
        printf("3. ɾ��Ա��\n");
        printf("4. �޸�Ա����Ϣ\n");
        printf("5. ͳ��Ա��������Ϣ\n");
        printf("6. �鿴����ְԱ��Ϣ\n");
        printf("7. �˳�\n");
        printf("��ѡ�����: ");
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
                // �ڳ������ǰ�������ݵ��ı��ļ�
                saveDataToFile();
                printf("�������˳���\n");
                break;
            default:
                printf("��Ч��ѡ�������ѡ��\n");
                break;
        }
    } while (choice != 7);

    return 0;
}
