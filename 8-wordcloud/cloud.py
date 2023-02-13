import jieba
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud

path = "D:\\python实训\\8-wordcloud\\关于进一步深化税收征管改革的意见.txt" # 词云文本的路径

with open(path, 'r', encoding="utf-8") as file:
    gaige = file.read() # 全部读取

jieba_str = jieba.lcut(gaige) # ['关于', '进一步', '深化', '税收', '征管', '改革', '的', '意见']
cut_text = " ".join(jieba_str)
# print(cut_text)
# print(jieba.lcut('关于进一步深化税收征管改革的意见'))
# 配置停用词，也就是要处理掉分词后的那些不太重要的词汇 比如 的， 你，我，和这种高频的  但是没有实际意义的词汇
# https://blog.csdn.net/luoluopan/article/details/114297744
stopwords = wordcloud.STOPWORDS
# stopwords.add('税务')
stopwords.add('的')
stopwords.add('和')
# stopwords.add('税收')
stopwords.add('你')
stopwords.add("我")
stopwords.add("吧")
stopwords.add("中国")


# 创建词云对象：1080p的画布
word_cloud = WordCloud(
    # 注意字体设置（win 自带字体库，选择自己需要的字体即可）
    font_path="C:/Windows/Fonts/simfang.ttf",
    background_color="white",  # 背景色 白色
    width=1920,  # 画布的宽度
    height=1080,  # 画布高度
    stopwords=stopwords,
    collocations=False).generate(cut_text)  # 生成 并传入文字

# 显示词云图
plt.imshow(word_cloud)
plt.axis('off') #关闭坐标轴
plt.show() # 右侧进行显示

# 保存词云图，文件名为 chinese_word_cloud.png
word_cloud.to_file("chinese_word_cloud.png")