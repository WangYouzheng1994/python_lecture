"""
jieba  结巴 是一个中文分词器

他的作用是分词：
可以将中文的文本通过分词获得单个词语，返回类型为列表类型。


https://blog.csdn.net/liujingwei8610/article/details/121758179 jieba

https://blog.51cto.com/cquptlei/6007705 wordcloud api解释
"""
import jieba
str="中国是一个伟大的国家"
# 精确模式是把文章词语精确的分开，并且不存在冗余词语，切分后词语总词数与文章总词数相同。
# 1 jieba 分词
print(jieba.lcut(str))

# 2 join 将序列（也就是字符串、元组、列表、字典）中的元素以指定的字符连接生成一个新的字符串
print(" ".join(str)) # 将 传入的list 按照指定的字符串进行拼接并分割
print("".join(str)) # 将 传入的list 按照指定的字符串进行拼接并分割