import os
import time
import sys
import shutil
import numpy
import datetime
lpSymbolA1 = os.path.exists("X:")  #判断是否A存在X盘符 返回布尔值t/f 定义X=迪卢克
lpSymbolA2 = os.path.exists("Y:")  #判断是否A存在Y盘符 返回布尔值t/f 定义Y=凯亚
lpSymbolA3 = os.path.exists("Z:")  #判断是否A存在X盘符 返回布尔值t/f 定义Z=砂糖
lpSymbolB1 = os.path.exists("L:")  #判断是否B存在L盘符 返回布尔值t/f 定义L=迪卢克
lpSymbolB2 = os.path.exists("M:")  #判断是否B存在M盘符 返回布尔值t/f 定义M=凯亚
lpSymbolB3 = os.path.exists("N:")  #判断是否B存在N盘符 返回布尔值t/f 定义N=砂糖

while True:
    print('\r','卡牌检测中…', end='')
    time.sleep(1)
    if lpSymbolA1 is True and lpSymbolA2 is True and lpSymbolA3 is True and lpSymbolB1 is True and lpSymbolB2 is True and lpSymbolB3 is True:
        print('\r','双方所有卡牌均已连接\n请稍候', end='')
        break
    else:
        print('\r','存在卡牌未连接，请检查磁吸触点是否清洁,5s后将重新检测', end='')
        time.sleep(5)

print('拷贝角色数据中')
shutil.copy('X:/A_diluke.txt', 'C:\\Users\\Administrator\\Desktop\\GameDocument\\A')
shutil.copy('Y:/A_kaiya.txt', "C:\\Users\\Administrator\\Desktop\\GameDocument\\A")
shutil.copy('Z:/A_shatang.txt', "C:\\Users\\Administrator\\Desktop\\GameDocument\\A")
shutil.copy('L:/B_diluke.txt', "C:\\Users\\Administrator\\Desktop\\GameDocument\\B")
shutil.copy('M:/B_kaiya.txt', "C:\\Users\\Administrator\\Desktop\\GameDocument\\B")
shutil.copy('N:/B_shatang.txt', "C:\\Users\\Administrator\\Desktop\\GameDocument\\B")


#以下为骰子录入，后期会改成图像识别#



