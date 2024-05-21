from bbs01 import *
from bbsNLP import *
from gettop import *

if __name__ == '__main__':
    top10 = gettop()
    for i in top10:
        url = 'https://bbs.pku.edu.cn/v2/' + i
        to = 'tmp/' + cut(i) + '.csv'
        get(url, to)
        nlp(to)