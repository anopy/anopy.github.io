import time
from 骰子录入 import Ashaizilist

yuansudir = {'1': '风', '2': '岩', '3': '雷', '4': '草', '5': '水', '6': '火', '7': '冰', '8': '万能'}  # 创建元素字典，不必再导入


def bestfriend():
    while True:
        chosed2shazi = input('你可以选择两个任意骰子，并将它们转化为两个万能骰子\n你选择的元素骰子：')
        if len(chosed2shazi) == 2:
            chosedlist = list(chosed2shazi)
            chosed1 = chosedlist[0]
            chosed2 = chosedlist[1]
            usedshaizi1 = yuansudir[chosed1]
            usedshaizi2 = yuansudir[chosed2]
            if usedshaizi1 in Ashaizilist and usedshaizi2 in Ashaizilist and usedshaizi1 == usedshaizi2:
                if Ashaizilist.count(usedshaizi1) >= 2:
                    Ashaizilist.remove(usedshaizi1)
                    Ashaizilist.remove(usedshaizi2)
                    Ashaizilist.append('万能')
                    Ashaizilist.append('万能')
                    break
                else:
                    print('你所选择的的元素骰子不足！重新输入！')
            elif usedshaizi1 in Ashaizilist and usedshaizi2 in Ashaizilist and usedshaizi1 != usedshaizi2:
                Ashaizilist.remove(usedshaizi1)
                Ashaizilist.remove(usedshaizi2)
                Ashaizilist.append('万能')
                Ashaizilist.append('万能')
                break
            else:
                print('你的所选择的元素骰子不足！重新输入！')
        else:
            print('你选择的骰子不足两个或超过两个，请重新输入')
            time.sleep(1.5)

while True:
    print('1：使用卡牌       2：普通攻击      3：元素技能      4：元素爆发      0：宣布回合结束')
    uuuchoice = input('你的选择：')
    if uuuchoice == '1':
        while True:
            capaiid = input('请输入你要使用的卡牌\n或者按n退出使用\n测试卡牌ID：')
            if capaiid == '001':
                if len(Ashaizilist) >= 2:
                    print('你打出了手牌：最好的伙伴！')
                    time.sleep(3)
                    print('你目前的拥有的元素骰子如下：', Ashaizilist)
                    print('编号列表：1：风 2：岩 3：雷 4：草 5：水 6：火 7：冰 8：万能')
                    bestfriend()
                    break
                else:
                    print('元素骰子不足！')
            elif capaiid == 'n':
                print('已退出')
                break
            else:
                print('没有对应的卡牌！重新输入！')
        break
    elif uuuchoice == '2':
        print('开发中……')
        break
    elif uuuchoice == '3':
        print('开发中……')
        break
    elif uuuchoice == '4':
        print('开发中……')
        break
    elif uuuchoice == '0':
        print('开发中……')
        break
    else:
        print('无效编号，重新输入！')

print('使用后的元素骰子：', Ashaizilist)
