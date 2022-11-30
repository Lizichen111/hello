import numpy as np   # 进行数据处理用到的库
import matplotlib.pyplot as plt  # 画图要用到的库

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
y = [174, 216, 255, 290, 325, 361, 399, 433, 460, 480, 495, 500, 502]

x = np.array(x)
y = np.array(y)

plot = plt.plot(x, y, 'b*', label='original values')
fit = np.polyfit(x, y, 2)  # 系数列表 这里1是一次拟合 如果改成2就是2次拟合，3次函数拟合的比较好。现在神经网络也可以用来拟合曲线，之所以拟合的好是因为参数多，次数高
print(fit)   # 输出的列表
p1 = np.poly1d(fit)  # 这里p1得到的是拟合的线
print("拟合曲线：", p1)
yvals = p1(x)
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.title('polyfit')  # 图片的标题
plt.legend()  # 图例
plt.savefig('曲线拟合.png')
plt.show()