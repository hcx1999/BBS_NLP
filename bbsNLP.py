import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import seaborn as sns

encode = 'utf-8'
#处理中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']})

def nlp(csv_file):

    # 读取文本数据，读取每行的评论标题
    orig_comments=pd.read_csv(csv_file)

    # print('原始数据:')
    # 输出前五行
    # print(orig_comments.head())
    # print(orig_comments)
    # print()

    # 使用SnowNLP计算对每条标题的文字评估情绪得分
    # 新建“情绪”一列
    orig_comments['emo']=None
    # 所有文本长度
    lenOrig=len(orig_comments)
    i=0
    # 计算情绪得分SnowNLP(数据二维表.iloc[行，列]).sentiments
    while(i<lenOrig):
        s=SnowNLP(orig_comments.iloc[i,0]).sentiments
        orig_comments.iloc[i,2]=s
        i=i+1
    
    # 输出每行的情绪得分
    print('情绪得分:')
    # 前五行
    # print(orig_comments.head())
    print(orig_comments)
    print()
    orig_comments.to_csv(csv_file, index = False)



if __name__ == '__main__':
    nlp('bbs18782037.csv')