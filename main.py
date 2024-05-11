from bbs01 import *
from bbsNLP import *

if __name__ == '__main__':
    url = 'https://bbs.pku.edu.cn/v2/post-read.php?bid=99&threadid=18782037'
    to = 'bbs数据清洗.csv'
    get(url, to)
    nlp(to)