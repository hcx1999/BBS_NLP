import requests
import re

encode = 'utf-8'

def cut(x):
    tmp = re.findall(r'\d+', x)
    return tmp[0] + '_' + tmp[1]

def gettop():

    url = 'https://bbs.pku.edu.cn/v2/home.php'

    # 下载网页内容
    response = requests.get(url)
    response.encoding = encode
    response.raise_for_status()  # 确保请求成功

    # 数据清洗处理
    cleaned_data = response.text
    cleaned_data = re.sub(r'&nbsp;', ' ', cleaned_data) #去除&nbsp;
    top10 = str(re.findall(r'<span class=\"rank-digit\">.*?</li>', cleaned_data))
    top10 = re.findall(r'<a class=\"post-link\" href=\".*?\"', top10) # 进一步提取
    for i in range(len(top10)):
        top10[i] = re.sub(r'<a class=\"post-link\" href=', '', top10[i])
        top10[i] = re.sub(r'amp;', '', top10[i])
        top10[i] = re.sub(r'\"', '', top10[i])

    return top10

def get_title():

    url = 'https://bbs.pku.edu.cn/v2/home.php'

    # 下载网页内容
    response = requests.get(url)
    response.encoding = encode
    response.raise_for_status()  # 确保请求成功

    # 提取标题
    title = response.text
    title = re.findall(r'<li><span class=\"rank-digit\">[0-9]+</span>.*?</li>', title)
    for i in range(len(title)):
        title[i] = re.sub(r'<.*?>', '', title[i])
        title[i] = re.sub(r'&nbsp;', ' ', title[i])

    return title


if __name__ == '__main__':
    # top10 = gettop()
    # print(gettop())

    title = get_title()
    print(title)