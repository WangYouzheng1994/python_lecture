### Numpy
> numpy是一个开源的科学计算库，支持常见的数组和矩阵操作。使用numpy比python原生api简单。
> numpy使用ndarray对象来处理多维数组，ndarray是一个速度快且灵活的大数据容器

1. numpy array的速度更快
- numpy array的限制是 只能存储同一类型的数据~
- ndarray 支持并行化运算（向量化运算）
- numpy底层使用了C语言编写，解除了GIL（全局解释锁），其数组的操作不受到python解释器的限制


### N维数组-adarray
1. 属性
- shape 数组维度的元祖
- ndim 数组维数
- size 元素个数
- itemsize 数组元素的长度
- dtype 数组元素的类型