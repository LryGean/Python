from operator import index
from PIL import Image
import numpy as np
import pandas as pd

size = [150,200]

filename = './p2.jpg'
im = Image.open(filename)
width, height = im.size
Lim = im.convert('L')
Lim = Lim.resize([150,200])

# 设置阈值转化为二值图，一般预览一下bim来调节
threshold = 170
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

bim = Lim.point(table, '1')

# 得到二值图矩阵
test = bim.getdata()
test1 = np.array(test)
test1 = test1.reshape(size[::-1])

pd.DataFrame(test1).to_csv('./lin.csv', index=None, header=None)