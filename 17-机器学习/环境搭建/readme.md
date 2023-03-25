1. 库的安装
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib==2.2.2
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy==1.14.2 
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas==0.20.3
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tables==3.4.2
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jupyter==1.0.0



pip --trusted-host pypi.python.org --trusted-host pypi.tuna.tsinghua.edu.cn install tables==3.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```
2. 批量安装库的方法
```
1. 批量执行以下脚本
pip install -r E:\wangyouzheng1994\python_lecture\17-机器学习\环境搭建\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

如果pycharm terminal报错：powershell因为在此系统上禁止运行脚本。
解决方案：
1. 然后找到windows上的Windows Powershall以管理员的身份运行下述命令
set-executionpolicy remotesigned
```



2. 解决tables装不上的问题
```
安装失败 did not find HDF5 headers
在安装某些 Python 库时，可能会遇到错误消息 "did not find HDF5 headers"。这通常是因为你的系统中没有安装 HDF5 库或者缺少 HDF5 库的头文件。
要解决这个问题，你需要安装 HDF5 库和头文件。以下是在 Ubuntu 上安装 HDF5 库和头文件的步骤：
打开终端并输入以下命令以安装 HDF5 库：sudo apt-get install libhdf5-serial-dev
输入密码并按回车键确认。
等待安装完成后，再次尝试安装 Python 库。
如果你使用的是其他操作系统，请参考相应的安装指南安装 HDF5 库和头文件。 作者：IBAS https://www.bilibili.com/read/cv22374330/ 出处：bilibili

https://www.hdfgroup.org/downloads/hdf5
账号：353735348@qq.com 老密码~
windows下解决此问题：
下载安装后，
设置 HDF5 环境变量。找到安装目录下的 bin 文件夹（例如：C:\Program Files\HDF_Group\HDF5\1.10.7\bin），将该文件夹路径添加到系统环境变量 PATH 作者：IBAS https://www.bilibili.com/read/cv22374330/ 出处：bilibili

```

小知识:
tables ：https://www.pytables.org/index.html  管理数据集
```
http://www.pytables.org/usersguide/installation.html
安装后测试
import tables
tables.test()
```
matplotlib: https://matplotlib.org/stable/ 画图的
```
https://matplotlib.org/stable/
```

