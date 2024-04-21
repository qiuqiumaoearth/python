#期望构建一个基于14个因素进行房价预测的模型
import numpy as np
import json
import pandas as pd

# #将xlsx文件进行转换变成csv文件
# excel_file='daima.xlsx'
# df=pd.read_excel(excel_file)#读取Excel文件

# csv_file='daima.csv'#指定CSV文件路径
# df.to_csv(csv_file,index=False)#index=False，表示不保存索引序列

#读取csv文件
# '''
# df=pd.read_csv('daima.csv',encoding='utf-8')
# print(df.head(3))#打印daima.csv文件的前3行
# '''
def load_data():
    '''读取波士顿房价的数据集'''
    data=pd.read_csv('boston.csv')
    #print(data)

    '''数据表示'''
    feature_names=['CRIM','ZN','INDUS','CHAS,NOX','RM,AGE','DIS','RAD','TAX','PIRATIO','B','LSTAT,MEDV']
    feature_nums=len(feature_names)

    '''将数据集中的80%作为训练集，20%作为测试集'''
    ratio=0.8
    a=data.shape #数据的行数和列数
    #print(a)
    offset=int(data.shape[0]*ratio)
    training_data = data[:offset]

    #数据归一化处理
    #计算train 数据的最大值，最小值，平均值
    maximums,minmums,avgs=training_data.max(axis=0),training_data.min(axis=0),training_data.sum(axis=0)/training_data.shape[0]
    #对数据归一化处理
    for i in range(feature_nums):
        print(minmums[i],maximums[i],avgs[i])

    #训练集和测试集的划分比例
    training_data=data[:offset]
    test_data=data[offset:]
    return training_data,test_data

    #获取数据
    training_data,test_data=load_data()
    x=training_data[:,:-1]
    y=training_data[:,-1:]

# w=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,-0.1,-0.2,-0.3,-0.4,0.0]
# w=np.array(w).reshape([13,1])
# print(w)


#完整的线性回归公式，还需要随意赋初值-0.2
#线性回归模型的完整输出是z=t+b ，这个从特征和参数计算输出值的过程称为“前向计算”
