import requests
import re

encode = 'utf-8'

def get(url, to_csv):

    # 下载网页内容
    response = requests.get(url)
    response.encoding = encode
    response.raise_for_status()  # 确保请求成功

    # 保存原始网页源码
    with open('bbs网页源码.txt', 'w', encoding = encode) as file:
        file.write(response.text)

    # 数据清洗处理
    cleaned_data = response.text
    cleaned_data = re.sub(r'&nbsp;', ' ', cleaned_data)   #去除&nbsp;
    cleaned_data = re.sub(r'\s+', ' ', cleaned_data)  # 去除多余的空白字符
    cleaned_data = re.findall(r'[0-9]*楼.*?</p>', cleaned_data) # 进一步提取
    cleaned_data = str(cleaned_data)   # 将list转换为str
    cleaned_data = re.sub(r'</p><p class=\'quotehead\'.*?>', '', cleaned_data)  #去除body
    cleaned_data = re.sub(r'<.*?>', '', cleaned_data)  # 去除HTML标签
    cleaned_data = re.sub(r'\', \'', '\n', cleaned_data)   # 去除列表标签
    cleaned_data = re.sub(r'楼主.*?\n', '*', cleaned_data)   #简化“楼主”标签
    cleaned_data = re.sub(r'^\[\'', '', cleaned_data)   #去除开头
    cleaned_data = re.sub(r'楼主\s+标题.*?\'\]', '', cleaned_data)   #去除结尾
    cleaned_data = re.sub(r'   ', ',', cleaned_data)

    # 保存清洗后的数据
    data_head = 'user,text\n'
    with open(to_csv, 'w', encoding = encode) as file:
        file.write(data_head + cleaned_data)

if __name__ == '__main__':
    url = 'https://bbs.pku.edu.cn/v2/post-read.php?bid=99&threadid=18782037'
    get(url)