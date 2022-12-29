import os
import time

yuansudir = {'1': '风', '2': '岩', '3': '雷', '4': '草', '5': '水', '6': '火', '7': '冰', '8': '万能'}  # 创建元素字典

while True:
    print(
        '请A独自录入骰子的元素\n参照实例：1：风 2：岩 3：雷 4：草 5：水 6：火 7：冰 8：万能\n则：若抽到了风 风 风 风 万能 雷 草 草 \n则输入：11118344')
    Ashai = input("输入你的骰子：")
    if len(Ashai) == 8 and '9' not in Ashai and '0' not in Ashai and ' ' not in Ashai:
        while True:
            if len(Ashai) == 8 and '9' not in Ashai and '0' not in Ashai and ' ' not in Ashai:
                shaizidaihao_listA = list(Ashai)
                shaizidaihao_listA.sort()  # 排序
                Ano1id = shaizidaihao_listA[0]  # 提取出用户输入的数字
                Ano2id = shaizidaihao_listA[1]
                Ano3id = shaizidaihao_listA[2]
                Ano4id = shaizidaihao_listA[3]
                Ano5id = shaizidaihao_listA[4]
                Ano6id = shaizidaihao_listA[5]
                Ano7id = shaizidaihao_listA[6]
                Ano8id = shaizidaihao_listA[7]
                Ano1 = yuansudir[Ano1id]  # 把用户输入的数字依照字典转换成文字
                Ano2 = yuansudir[Ano2id]
                Ano3 = yuansudir[Ano3id]
                Ano4 = yuansudir[Ano4id]
                Ano5 = yuansudir[Ano5id]
                Ano6 = yuansudir[Ano6id]
                Ano7 = yuansudir[Ano7id]
                Ano8 = yuansudir[Ano8id]
                Ashaizilist = [Ano1, Ano2, Ano3, Ano4, Ano5, Ano6, Ano7, Ano8]  # 创建文字列表，后续操作基于文字列表
                print('你的骰子如下：', Ashaizilist)
                time.sleep(2)
                print('若确认无误，则输入y以继续；若要返回修改，请输入n以重新输入')
                ans = input('请输入：')
                if ans == 'y':
                    print('\r', '您已写入完成，请稍候', end='')
                    break
                elif ans == 'n':
                    Ashaizilist.clear()
                    Ashai = input("输入你的骰子：")
                else:
                    print('输入有误！重新输入')
            else:
                print('骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！')
                Ashai = input("输入你的骰子：")
        break
    else:
        print('骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！')

os.system('cls')

print('已经清屏保密，现在请B独自输入骰子的元素')

while True:
    print('参照实例：1：风 2：岩 3：雷 4：草 5：水 6：火 7：冰 8：万能\n则：若抽到了风 风 风 风 万能 雷 草 草 \n则输入:11118344')
    Bshai = input("输入你的骰子：")
    if len(Bshai) == 8 and '9' not in Bshai and '0' not in Bshai and ' ' not in Bshai:
        while True:
            if len(Bshai) == 8 and '9' not in Bshai and '0' not in Bshai and ' ' not in Bshai:
                shaizidaihao_listB = list(Bshai)
                shaizidaihao_listB.sort()  # 排序
                Bno1id = shaizidaihao_listB[0]
                Bno2id = shaizidaihao_listB[1]
                Bno3id = shaizidaihao_listB[2]
                Bno4id = shaizidaihao_listB[3]
                Bno5id = shaizidaihao_listB[4]
                Bno6id = shaizidaihao_listB[5]
                Bno7id = shaizidaihao_listB[6]
                Bno8id = shaizidaihao_listB[7]
                Bno1 = yuansudir[Bno1id]
                Bno2 = yuansudir[Bno2id]
                Bno3 = yuansudir[Bno3id]
                Bno4 = yuansudir[Bno4id]
                Bno5 = yuansudir[Bno5id]
                Bno6 = yuansudir[Bno6id]
                Bno7 = yuansudir[Bno7id]
                Bno8 = yuansudir[Bno8id]
                Bshaizilist = [Bno1, Bno2, Bno3, Bno4, Bno5, Bno6, Bno7, Bno8]
                print('你的骰子如下：', Bshaizilist)
                time.sleep(2)
                print('若确认无误，则输入y以继续；若要返回修改，请输入n以重新输入')
                ans2 = input('请输入：')
                if ans2 == 'y':
                    print('\r', '您已写入完成，请稍候', end='')
                    break
                elif ans2 == 'n':
                    Bshai = input("输入你的骰子：")
                else:
                    print('输入有误！重新输入')
            else:
                print('骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！！')
                Bshai = input("输入你的骰子：")
        break
    else:
        print('骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！')
os.system('cls')

print('已清屏，正在写入数据')
time.sleep(2)
print('骰子录入部分已完成')
