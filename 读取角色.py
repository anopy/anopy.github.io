#该模块包含内容：检查卡牌连接、复制角色文件至桌面文件夹、

import os
import shutil
import time

lpSymbolA1 = os.path.exists("O:")  # 判断是否A存在O盘符 返回布尔值t/f 定义X=迪卢克
lpSymbolA2 = os.path.exists("P:")  # 判断是否A存在P盘符 返回布尔值t/f 定义Y=凯亚
lpSymbolA3 = os.path.exists("Q:")  # 判断是否A存在Q盘符 返回布尔值t/f 定义Z=砂糖
lpSymbolB1 = os.path.exists("L:")  # 判断是否B存在L盘符 返回布尔值t/f 定义L=迪卢克
lpSymbolB2 = os.path.exists("M:")  # 判断是否B存在M盘符 返回布尔值t/f 定义M=凯亚
lpSymbolB3 = os.path.exists("N:")  # 判断是否B存在N盘符 返回布尔值t/f 定义N=砂糖

while True:
    print('\r', '卡牌检测中…', end='')
    time.sleep(1)
    if lpSymbolA1 is True and lpSymbolA2 is True and lpSymbolA3 is True and lpSymbolB1 is True and lpSymbolB2 is True and lpSymbolB3 is True:
        print('\r', '双方所有卡牌均已连接\n请稍候', end='')
        break
    else:
        print('\r', '存在卡牌未连接，请检查触点是否清洁，5s后将重新检测', end='')
        time.sleep(5)
time.sleep(1.5)

print('拷贝角色数据中')

# ！！！！！！！！！！！！！！！！！！！！！！！！！！
# 缺少新建游戏数据文件夹#
# ！！！！
# ！！！！！！！！！！！！！！！！！！！！！！


srcA1 = "O:\\Characters"  # 源文件目录
srcA2 = "P:\\Characters"  # 源文件目录
srcA3 = "Q:\\Characters"  # 源文件目录
srcB1 = "L:\\Characters"  # 源文件目录
srcB2 = "M:\\Characters"  # 源文件目录
srcB3 = "N:\\Characters"  # 源文件目录
detA = "C:\\Users\imooc\Desktop\Game Documents\A"  # 目的文件目录
detB = "C:\\Users\imooc\Desktop\Game Documents\B"  # 目的文件目录
for root, _, fnames in os.walk(srcA1):
    for fname in sorted(fnames):  # sorted函数把遍历的文件按文件名排序
        fpath = os.path.join(root, fname)
        shutil.copy(fpath, detA)  # 把所有文件全部复制进det目录
        print(fname + " has been copied!")
for root, _, fnames in os.walk(srcA2):
    for fname in sorted(fnames):  # sorted函数把遍历的文件按文件名排序
        fpath = os.path.join(root, fname)
        shutil.copy(fpath, detA)  # 把所有文件全部复制进det目录
        print(fname + " has been copied!")
for root, _, fnames in os.walk(srcA3):
    for fname in sorted(fnames):  # sorted函数把遍历的文件按文件名排序
        fpath = os.path.join(root, fname)
        shutil.copy(fpath, detA)  # 把所有文件全部复制进det目录
        print(fname + " has been copied!")
for root, _, fnames in os.walk(srcB1):
    for fname in sorted(fnames):  # sorted函数把遍历的文件按文件名排序
        fpath = os.path.join(root, fname)
        shutil.copy(fpath, detB)  # 把所有文件全部复制进det目录
        print(fname + " has been copied!")
for root, _, fnames in os.walk(srcB2):
    for fname in sorted(fnames):  # sorted函数把遍历的文件按文件名排序
        fpath = os.path.join(root, fname)
        shutil.copy(fpath, detB)  # 把所有文件全部复制进det目录
        print(fname + " has been copied!")
for root, _, fnames in os.walk(srcB3):
    for fname in sorted(fnames):  # sorted函数把遍历的文件按文件名排序
        fpath = os.path.join(root, fname)
        shutil.copy(fpath, detB)  # 把所有文件全部复制进det目录
        print(fname + " has been copied!")