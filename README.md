我的名字是巨田田，从今天起，我开始翻译整理matplotlib库的东西，如果有小伙伴愿意加入，欢迎欢迎，我的微信号dadada_xiao.

千里之行，始于足下，我们开始吧

https://matplotlib.org/    是打算翻译的内容来源.

在我们实验室，我们使用267nm波长100fs的脉冲激光作为电离源，电离产生的分子离子，碎片离子被飞行时间质谱仪进行离子质量分析，从而确定这个化合物是什么。如下图所示，这种信号处理方式是模拟信号
![image](https://github.com/kuzhenzhen/matplotlib-/blob/master/Picture1.png)


如今在我们研究室更新换代了，借鉴了时间相关单光子检测系统，为了更深入的研究多光子电离和提高检出限，

正在做的课题是模拟转数字信号，经过时间的累积信号，得到更好的信噪比，从而达到超低浓度的检测，然而我到现在还没写paper。就让我悲伤逆流成河。。。


![image](https://github.com/kuzhenzhen/matplotlib-/blob/master/Picture2.png)

现在，进的样品是五氯苯，因为氯原子有同位素分子 CL:35,CL:37, 所以五氯苯会有五个氯原子的同位素峰，如下图所示：
![image](https://github.com/kuzhenzhen/matplotlib-/blob/master/%E5%9B%BE3-2%E9%99%84%E5%B8%A6%E6%B3%A8%E9%87%8A.jpg)


以上是背景，分析化学领域的飞秒激光电离和飞行时间质谱仪串联分析，，，这颗分析化学领域冉冉升起的新星无奈沦落为背景板

以下才是正题，我最最喜欢的Python，写了数据处理分析软件，当我写的代码能正常运行的时候，我觉得自己简直就是一个不出世的天才

从原始数据开始吧

2017-12-15T11-56-31.awd是数据文件

图1是我们研究室中村先生写的软件，用于分析这个数据。我超级超级敬佩中村教授，发自肺腑的敬佩，高山仰止

![image](https://github.com/kuzhenzhen/matplotlib-/blob/master/%E5%9B%BE1.png)

图2是Excel表格做出来的图，也可以用于分析这个数据，就是全选复制粘贴有些费劲，用于比较。

![image](https://github.com/kuzhenzhen/matplotlib-/blob/master/%E5%9B%BE2.png)

图3是我用Python写的程序，使用了matplotlib作为画图利器。边学边写代码，我个人喜欢按目的去学。漫无边际的学的话，很容易迷失在知识的汪洋大海里面。

![image](https://github.com/kuzhenzhen/matplotlib-/blob/master/%E5%9B%BE3-1.png)

![image](https://github.com/kuzhenzhen/matplotlib-/blob/master/%E5%9B%BE3-2.png)

写这个程序主要由4个部分：

1.导入matplotlib，numpy的库

2.读取文件的数据

3.读取数据之后因为是字符串，调用pyplot里面的函数画图的时候就会报错，所以要写一个循环，是的每个字符串都转换成数值。

4.使用matplotlib画图，使用matplotlib.pyplot画图。

OK,是不是很简单，看伪代码是不是很简单，其实真代码也简单。见DA.py



下面详细介绍DA.py的源码。


1.导入matplotlib，numpy的库


import numpy as np

import matplotlib.pyplot as plt 


2.读取文件的数据，我的数据格式是这样的：2017-12-15T11-56-31.awd

-2

-5

-6

-4

-7

-7

-8

-15

-24

-63

-83

-152

-199

-313

-438

-557

-703

-743

-791

-794

-728

-604

-475


所以就比较容易。


代码如下：


filename = '2017-12-15T11-56-31.awd'

fileName = open(filename, 'r')

lines = fileName.read().splitlines()


3.读取数据之后因为是字符串，调用pyplot里面的函数画图的时候就会报错，所以要写一个循环，是的每个字符串都转换成数值。


newLines = []

for  linesLetter in lines:

b = int(linesLetter)

newLines.append(b)


4.使用matplotlib画图，使用matplotlib.pyplot画图。


l1=plt.plot(newLines,'r--',label='Pentachlorobenzene')

plt.title('267 nm 100 fs laser ionization for Pentachlorobenzene using TOFMS')

plt.xlabel('channel')

plt.ylabel('intensity')

plt.legend()

plt.show()
