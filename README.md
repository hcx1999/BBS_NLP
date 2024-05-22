# 问题求解与程序设计 小组作业

## 目前已完成：

提供GUI图形界面，爬取bbs评论区并对其进行情绪评分，支持查看情绪得分统计柱形图，支持查看原网页，支持查看具体每一条具体帖子内容。

先由`gettop.py`爬取前十条的url和标题并保存。

由`bbsWash.py`最近`未名BBS`的评论并进行清洗，得到以网页bid_threadid命名的csv文件，储存在csv文件夹中。

由`bbsNLP.py`使用SnowNLP对清洗处理过的文本进行情绪评分，并保存原文件中。

优化了换行bug，但是由于代码基于网页源码清洗来判断发帖内容，所以理论上可能会有些帖子的内容会引起报错。但只要不是故意，报错的概率几乎为0。

## 使用方法：

使用时，运行`main.py`，即可爬取热门前十的bbs版面。

可能的用处：大学生心理健康与各种因素的关系分析；应用一个语言模型来训练另一个……由于本项目是一个可扩展性很强的基础项目，因此并没有很多直接的应用，但是可以与其他学科（如人文社科）进行交叉，提供情绪分析评分的功能。

相比SnowNLP的直接评分，我进行了简单的优化，即`折合分 = 原始分 * 100 - 33`，使情绪评分更直观。

## 遇到的问题以及后期方向：

1.得到的数据有什么贴近生活的或者比较有意义的应用吗？

2.能否设置范围进行实时爬取？（已解决！）

## 需要预先下载的库：

```bash
pip install matplotlib
pip install webbrowser
pip install pandas
pip install openpyxl
pip install requests
pip install snownlp
pip install seaborn
```

## 参考文献：

[1] 钟雪灵等.Python金融数据挖掘[M].北京：高等教育出版社，2020：132.

[2] 基于汉语分词的文本情感分析系统 [SnowNLP](https://github.com/isnowfy/snownlp)
