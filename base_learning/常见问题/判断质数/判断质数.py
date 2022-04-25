import math
num = 211

def checkP(num):
    flag = True
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            flag = False
            break
    return flag

print(checkP(num))


## 向下取整 int ——> int(3.75)=3

## 向上取整 math.ceil ——> math.ceil(3.75)=4.0

## 四舍五入 round ——> round(3.25)=3.0, round(3.75)=4.0