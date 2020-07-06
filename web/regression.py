from matplotlib.ticker import MultipleLocator

from web import taobao
import re
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simfang.ttf")
from sklearn.linear_model import LinearRegression #创建拟合模型#
import numpy as np



list = taobao.get_list("拖把")
X = []
y = []
for i in range(len(list)):
    spu = list[i]
    X.append(float(spu[2]))
    sales = spu[5]
    sales = re.findall('(.*?)万', sales)
    y.append(float(sales[0]))
plt.figure(figsize=(16, 8))
plt.title('LINE1', fontproperties=font)
plt.xlabel('价格', fontproperties=font)
plt.ylabel('销量', fontproperties=font)

plt.xlim(0,200)
plt.scatter(X,y,c='black')
plt.show()
z = zip(X,y)
model = LinearRegression()
x,y=z[:,0].reshape(-1,1),z[:,1]
model.fit(x,y)
print('12prices:$%.2f'% model.predict(12))

