"""
认识代码的包
1. 新建一个 package
2. package中会出现一个__init__.py的文件，这个文件的存在就决定了 这是一个 package
3. 纠正青岛的ppt：python 没有严格意义的库的概念，因为一个module（python文件可以是一个库，但是一个package下面多个module 组成也可以是一个库~）
4. __init__.py中限制import 自行百度
"""

"""
一个包就是同类型的功能集合体
numpy 科学计算
pandas 数据分析 
tensorflow 人工智能

他们丰富了整个python的生态，因为这一堆包的存在 才让python变得好用
"""

# 1 使用pip 安装外部包
"""
1. 命令行中 运行：pip install 包名
2. 镜像站加快速度

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
"""

"""
问题解决：
ERROR: Could not install packages due to an OSError: [WinError 2] 系统找不到指定的文件。: ‘C:\Python310\Scripts\f2py.exe’ -> ‘C:\Python310\Scripts\f2py.exe.deleteme’
pip install --user package 

————————————————
版权声明：本文为CSDN博主「CallMeAnonymity」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_40301746/article/details/124017100
"""