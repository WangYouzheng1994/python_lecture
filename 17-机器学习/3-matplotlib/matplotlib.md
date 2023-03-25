#### matplotlib
```
import matplotlib.pyplot as plt

# 画布
plt.figure(figsize=(20,8), dpi=100);
# 图像绘制
x = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.plot(x, y)

# 展示
plt.show()
```

matplotlib三层结构组成部分
- Canvas，画板
- figure画板的上层（画布）
- axes绘图区

在Axes中又有具体的角色
- Figure 通过Figure设置画布的大小和分辨率（plt.figure）
- Axes ：数据绘图区
- Axis：坐标系轴，设置单位、大小等数据

整体来看：一个figure可以有多个Axes。一个Axes只能隶属于一个Figure （一个画布有多个绘图区）
一个axes（绘图区）可以有多个坐标系（axis），两个axis就是2d坐标，即XY轴。三个zxis就是三个坐标


#### 解决matplotlib英文乱码问题
1. 需要电脑中有对应的字体
```
linux 安装字体：
拷贝到 usr/share/fonts中
cp /opt/SimHei.ttf /usr/share/fonts/SimHei.ttf

删除~/.matplotlib中的缓存
rm -r ~/.matplotlib

```
2. 方案1：全局修改
```
vim ~/.matplotlib/matplotlibrc修改配置文件如下：
font.family:sans-serif
font.sans-serif:SimHei
axes.unicode_minus:false
```

3. 方案2：代码解决
```
# 解决中文报错问题。
plt.rcParams['font.sans-serif']=['SimHei']
```