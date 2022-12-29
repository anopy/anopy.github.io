import binascii
import os
import random
import time

import serial.tools.list_ports

# 以下为PN532各功能16进制指令转换hex

send_wake_up_hex = bytes.fromhex('55 55 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff 03 fd d4 14 01 17 00')
send_read_id_hex = bytes.fromhex('00 00 FF 04 FC D4 4A 02 00 E0 00')

# 以下为各个角色基本信息表
name_to_full_yuansuchongneng ={'迪卢克':'3','凯亚':'2','砂糖':'2'}     # 定义字典，把角色名称与元素充能最大数相联系
id_to_full_yuansuchongneng = {'000001':'3','000002':'2','000003':'3'}   # 定义字典，把角色id与元素充能最大数相联系
id_to_basic_attack_blood = {'000001':'2','000002':'2','000003':'1'}     # 把角色id与普通攻击扣除血量联系起来
id_to_basic_attack_yuansu = {'000001':'','000002':'','000003':'风'}      # 把id与普通攻击附着的元素联系起来
id_to_basic_attack_zhiding_shaiziname = {'000001':'火','000002':'冰','000003':'风'}        # 把id和普通攻击消耗的本身指定元素骰子数量联系起来
id_to_basic_attack_wuse_shaizi_num = {'000001':'2','0000002':'2','000003':'2'}          # id与普通攻击消耗无色元素数量联系
id_to_yuansu_attack_blood = {'000001':'3','000002':'3','000003':'3'}                    # id与e技能攻击伤害联系起来
id_to_yuansu_attack_zhiding_shaiziname = {'000001':'火','000002':'冰','000003':'风'}       # id与e技能攻击所需要的骰子种类联系
id_to_yuansu_attack_zhiding_shaizi_num = {'000001':'3','0000002':'3','000003':'3'}      # id与e技能攻击所需要的指定元素骰子数量联系

print('加载中，请稍候')

print('欢迎你，现在，请按照提示进行设备基本设置吧！')
time.sleep(3)
print('首先，请打开1-4号开关，关闭其他开关，并移除设备上所有的角色卡牌与手牌，完成后请按任意键继续')
os.system('pause')

# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
pliststr = str(plist)
time.sleep(1)
print('\r', '好的，现在，请关闭所有开关，按任意键以配置读卡器。', end='')
os.system('pause')
print('配置A1读卡器')
time.sleep(3)
print(plist)
print('以上为原始列表，现在打开A1读卡器')
os.system('pause')
print('请稍候')
time.sleep(5)
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
print(plist)
print('以上为刷新后的列表')
ser1 = input('A1端口：')

print('打开A2读卡器，按任意键继续')
os.system('pause')
print('请稍候')
time.sleep(5)
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
print(plist)
print('以上为刷新后的列表')
ser2 = input('A2端口：')

print('打开A3读卡器，按任意键继续')
os.system('pause')
print('请稍候')
time.sleep(5)
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
print(plist)
print('以上为刷新后的列表')
ser3 = input('A3端口：')

print('打开B1读卡器，按任意键继续')
os.system('pause')
print('请稍候')
time.sleep(5)
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
print(plist)
print('以上为刷新后的列表')
ser4 = input('B1端口：')

print('打开B2读卡器，按任意键继续')
os.system('pause')
print('请稍候')
time.sleep(5)
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
print(plist)
print('以上为刷新后的列表')
ser5 = input('B2端口：')

print('打开B3读卡器，按任意键继续')
os.system('pause')
print('请稍候')
time.sleep(5)
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
print(plist)
print('以上为刷新后的列表')
ser6 = input('B3端口：')

print('打开手牌读卡器，按任意键继续')
os.system('pause')
print('请稍候')
time.sleep(5)
# 获取所有串口设备实例。
# 如果没找到串口设备，则输出：“无串口设备。”
# 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("无串口设备，请检查CH340驱动是否安装，USB线缆是否牢固连接，按任意键退出重试")
    os.system('pause')
    exit(0)
else:
    plist = []
    cckkll = 0
    for comport in ports_list:
        cckkll = cckkll + 1
        plist.append(str(comport))
print(plist)
print('以上为刷新后的列表')
ser7 = input('手牌端口：')

os.system('cls')

print('串口绑定已完成，现在开始测试A1，在A1上放置一张卡')
os.system('pause')
print('尝试读卡中……')
Aser1 = serial.Serial(ser1, 115200)
if Aser1.isOpen():
    print('A1串口已打开')
else:
    print('串口打开失败！请退出并联系开发者')
    os.system('pause')
    Aser1.close()
    exit(0)
Aser1.write(send_wake_up_hex)
wkup_answer_A1 = Aser1.inWaiting()
time.sleep(0.5)
Aser1.write(send_read_id_hex)
test_answer_A1 = Aser1.inWaiting()
if test_answer_A1 is not None:
    testdata = str(binascii.b2a_hex(Aser1.read(test_answer_A1)))[2:-1]
    print('读取数据:', testdata)
    Aser1.close()
else:
    print('未读到数据！请退出重试！')
    os.system('pause')
    Aser1.close()
    exit(0)

print('测试完成，初始化成功')

time.sleep(3)
os.system('cls')

character_id_to_name_dir = {'000001': '迪卢克',
                            '000002': '凯亚',
                            '000003': '砂糖'}  # 共享字典，存储所有的ID对角色名称，后期改为卡ID
name_to_character_id_dir = {'迪卢克': '000001',
                            '凯亚': '000002',
                            '砂糖': '000003'}  # 共享字典，存储所有的ID对角色名称，后期改为卡ID


while True:
    print('请A方将3张角色卡分别放在A1、A2、A3读卡器上，完成后请按任意键继续……')
    os.system('pause')
    print('读卡中……')
    time.sleep(0.5)
    Aser2 = serial.Serial(ser2, 115200)
    Aser3 = serial.Serial(ser3, 115200)
    Bser1 = serial.Serial(ser4, 115200)
    Bser2 = serial.Serial(ser5, 115200)
    Bser3 = serial.Serial(ser6, 115200)
    spser = serial.Serial(ser7, 115200)

    Aser1.write(send_read_id_hex)
    id_answer1_hex = Aser1.inWaiting()
    id_answer1 = str(binascii.b2a_hex(id_answer1_hex))[2:-1]

    Aser2.write(send_read_id_hex)
    id_answer2_hex = Aser2.inWaiting()
    id_answer2 = str(binascii.b2a_hex(id_answer2_hex))[2:-1]

    Aser3.write(send_read_id_hex)
    id_answer3_hex = Aser3.inWaiting()
    id_answer3 = str(binascii.b2a_hex(id_answer3_hex))[2:-1]
    Acharacter1_id = str(id_answer1)  # 后期此处为读卡识别的ID
    Acharacter2_id = str(id_answer2)
    Acharacter3_id = str(id_answer3)
    character_id_pool = [Acharacter1_id, Acharacter2_id, Acharacter3_id]
    if Acharacter1_id == Acharacter2_id or Acharacter1_id == Acharacter3_id or Acharacter2_id == Acharacter3_id:
        print('三个角色必须互不相同！请重新刷卡！')
    else:
        if Acharacter1_id in character_id_to_name_dir and Acharacter2_id in character_id_to_name_dir and Acharacter3_id in character_id_to_name_dir:
            break
        else:
            print('未找到该卡牌，请重新刷卡！')

os.system("cls")  # 清空cmd
Ach1 = character_id_to_name_dir[Acharacter1_id]
Ach2 = character_id_to_name_dir[Acharacter2_id]
Ach3 = character_id_to_name_dir[Acharacter3_id]

Ayuansu1 = []  # 1\2\3角色所附着元素，单字,用列表存储
Ayuansu2 = []
Ayuansu3 = []

Ach1_blood = 10  # 1、2、3角色血量变量，每局开始前 = 10
Ach2_blood = 10
Ach3_blood = 10
# 以上为A方出战角色、元素附着、血量定义，仅做测试1

while True:
    print('角色列表：', '1:', Ach1, '2:', Ach2, '3:', Ach3)
    A_main_cha_num = input('选择出战角色编号：')
    if A_main_cha_num == '1':
        A_main_character = Ach1
        os.system('cls')
        break
    elif A_main_cha_num == '2':
        A_main_character = Ach2
        os.system('cls')
        break
    elif A_main_cha_num == '3':
        A_main_character = Ach3
        os.system('cls')
        break
    else:
        print('不存在此角色！请重新输入！')

print('     ', Ach1, '           ', Ach2, '          ', Ach3, '          ''\n''     ', '[', Ach1_blood, ']',
      '         ', '[', Ach2_blood, ']', '        ', '[', Ach3_blood, ']')

if len(Ayuansu1) > 0 or len(Ayuansu2) > 0 or len(Ayuansu3) > 0:
    print('     ', Ayuansu1, '           ', Ayuansu2, '           ', Ayuansu3)

if A_main_character == Ach1:
    print('       出战')
elif A_main_character == Ach2:
    print('                        出战')
else:
    print('                                        出战')

# 以上为A方出战角色信息输出UI
print('\n\n以上为输出测试，按任意键继续')
os.system('pause')
os.system('cls')

while True:
    print('请B方将3张角色卡分别放在A1、A2、A3读卡器上，完成后请按任意键继续……')
    os.system('pause')
    print('读卡中……')
    time.sleep(0.5)
    Bser1 = serial.Serial(ser4, 115200)
    Bser2 = serial.Serial(ser5, 115200)
    Bser3 = serial.Serial(ser6, 115200)
    spser = serial.Serial(ser7, 115200)

    Bser1.write(send_read_id_hex)
    id_answer4_hex = Bser1.inWaiting()
    id_answer4 = str(binascii.b2a_hex(id_answer4_hex))[2:-1]

    Bser2.write(send_read_id_hex)
    id_answer5_hex = Bser2.inWaiting()
    id_answer5 = str(binascii.b2a_hex(id_answer5_hex))[2:-1]

    Bser3.write(send_read_id_hex)
    id_answer6_hex = Bser3.inWaiting()
    id_answer6 = str(binascii.b2a_hex(id_answer6_hex))[2:-1]
    Bcharacter1_id = str(id_answer4)  # 后期此处为读卡识别的ID
    Bcharacter2_id = str(id_answer5)
    Bcharacter3_id = str(id_answer6)
    character_id_pool = [Bcharacter1_id, Bcharacter2_id, Bcharacter3_id]
    if Bcharacter1_id == Bcharacter2_id or Bcharacter1_id == Bcharacter3_id or Bcharacter2_id == Bcharacter3_id:
        print('三个角色必须互不相同！请重新刷卡！')
    else:
        if Bcharacter1_id in character_id_to_name_dir and Bcharacter2_id in character_id_to_name_dir and Bcharacter3_id in character_id_to_name_dir:
            break
        else:
            print('未找到该卡牌，请重新刷卡！')

os.system("cls")  # 清空cmd
Bch1 = character_id_to_name_dir[Bcharacter1_id]
Bch2 = character_id_to_name_dir[Bcharacter2_id]
Bch3 = character_id_to_name_dir[Bcharacter3_id]

Byuansu1 = []  # 1\2\3角色所附着元素，单字,用列表存储
Byuansu2 = []
Byuansu3 = []

Bch1_blood = 10  # 1、2、3角色血量变量，每局开始前 = 10
Bch2_blood = 10
Bch3_blood = 10
# 以上为A方出战角色、元素附着、血量定义，仅做测试1

while True:
    print('角色列表：', '1:', Bch1, '2:', Bch2, '3:', Bch3)
    main_cha_num = input('选择出战角色编号：')
    if main_cha_num == '1':
        B_main_character = Bch1
        os.system('cls')
        break
    elif main_cha_num == '2':
        B_main_character = Bch2
        os.system('cls')
        break
    elif main_cha_num == '3':
        B_main_character = Bch3
        os.system('cls')
        break
    else:
        print('不存在此角色！请重新输入！')

print('     ', Bch1, '           ', Bch2, '          ', Bch3, '          ''\n''     ', '[', Bch1_blood, ']',
      '         ', '[', Bch2_blood, ']', '        ', '[', Bch3_blood, ']')

if len(Byuansu1) > 0 or len(Byuansu2) > 0 or len(Byuansu3) > 0:
    print('     ', Byuansu1, '           ', Byuansu2, '           ', Byuansu3)

if B_main_character == Bch1:
    print('       出战')
elif B_main_character == Bch2:
    print('                        出战')
else:
    print('                                        出战')

# 以上为B方出战角色信息输出UI
print('\n\n以上为输出测试，按任意键继续')
os.system('pause')

os.system('cls')
print('角色选择已完成！加载中……')

os.system('cls')
print('请A、B分别从自己的卡堆中抽出5张手牌，并防止对方知晓，完成后按任意键继续')
os.system('pause')

os.system('cls')
print('投掷阶段\n接下来，请双方独自掷骰子，投掷结果不要让别人看到，掷完后按任意键继续')
os.system('pause')

yuansudir = {'1': '风', '2': '岩', '3': '雷', '4': '草', '5': '水', '6': '火', '7': '冰', '8': '万能'}  # 创建元素字典

while True:
    print(
        '请A独自录入骰子的元素\n参照实例：1：风 2：岩 3：雷 4：草 5：水 6：火 7：冰 8：万能\n则：若抽到了风 风 风 风 万能 雷 草 草 \n则输入：11118344\n不要输入空格、标点！')
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
                print(
                    '骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！')
                Ashai = input("输入你的骰子：")
        break
    else:
        print(
            '骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！')

os.system('cls')

print('已经清屏保密，现在请B独自输入骰子的元素')

while True:
    print(
        '参照实例：1：风 2：岩 3：雷 4：草 5：水 6：火 7：冰 8：万能\n则：若抽到了风 风 风 风 万能 雷 草 草 \n则输入:11118344\n不要输入空格、标点！')
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
                print(
                    '骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！！')
                Bshai = input("输入你的骰子：")
        break
    else:
        print(
            '骰子数目应该等于8个！或者你输入了没有定义的数字（例如 9 0）!要不就是你手贱多打了空格、标点之类的！（反正就是不对（确信））请重新输入！')
os.system('cls')

print('已清屏，正在写入数据')
time.sleep(2)
print('骰子录入部分已完成，请按任意键继续……')
os.system('pause')

os.system('cls')
print('游戏正式开始！现在将随机指派先后手，生成随机数中……')
xianshou = random.randint(0, 1)
time.sleep(0.5)
if xianshou == 0:
    print('本次游戏A方先手！')
    first = 'A'
    second = 'B'
else:
    print('本局游戏B方先手！')
    first = 'B'
    second = 'A'
time.sleep(2)
os.system('cls')
print('行动阶段')

Acharacter1_yuansuchongneng = 0
Acharacter2_yuansuchongneng = 0
Acharacter3_yuansuchongneng = 0
Bcharacter1_yuansuchongneng = 0
Bcharacter2_yuansuchongneng = 0
Bcharacter3_yuansuchongneng = 0

if A_main_character == Ach1:
    Amain_character_yuansuchongneng = Acharacter1_yuansuchongneng
elif A_main_character == Ach2:
    Amain_character_yuansuchongneng = Acharacter2_yuansuchongneng
elif A_main_character == Ach3:
    Amain_character_yuansuchongneng = Acharacter3_yuansuchongneng

def firststage():  # 这是一级菜单
    print('----Menu----'
          '\n1.普通攻击'
          '\n2.元素战技'
          '\n3.元素爆发   当前元素充能：', Amain_character_yuansuchongneng, '/', '3'
          '\n4.使用手牌'
          '\n5.手牌转换元素骰子'
          '\n6.切换角色'
          '\n0.宣布回合结束')


def UIprint():
    print('     ', Ach1, '           ', Ach2, '          ', Ach3, '          ''\n''     ', '[', Ach1_blood, ']',
          '         ', '[', Ach2_blood, ']', '        ', '[', Ach3_blood, ']')

    if len(Ayuansu1) > 0 or len(Ayuansu2) > 0 or len(Ayuansu3) > 0:
        print('     ', Ayuansu1, '           ', Ayuansu2, '           ', Ayuansu3)

    if A_main_character == Ach1:
        print('       出战')
    elif A_main_character == Ach2:
        print('                        出战')
    else:
        print('                                        出战')

    print('\n\n\n\n')
    print('     ', Bch1, '           ', Bch2, '          ', Bch3, '          ''\n''     ', '[', Bch1_blood, ']',
          '         ', '[', Bch2_blood, ']', '        ', '[', Bch3_blood, ']')

    if len(Byuansu1) > 0 or len(Byuansu2) > 0 or len(Byuansu3) > 0:
        print('     ', Byuansu1, '           ', Byuansu2, '           ', Byuansu3)

    if B_main_character == Bch1:
        print('       出战')
    elif B_main_character == Bch2:
        print('                        出战')
    else:
        print('                                        出战')

while True:
    os.system('cls')
    UIprint()
    print('\n\n\n\n')
    print('请',first,'方行动')
    firststage()
    uuucho = input('输入行动编号：')

    if uuucho == '1':
        A_main_cha_id = name_to_character_id_dir[A_main_character]      # A出战角色的系统ID（000001-000003）
        print('你将要进行：普通攻击')
        print('本次共计消耗：',)       # 在那一堆字典里找出来普通攻击需要消耗的元素骰子，输出格式："本次共计消耗：1个火元素骰 + 2个无色元素骰子，请输入要消耗的无色骰子。"并打印输出当前骰子列表
    elif uuucho == '2':
        print()
    elif uuucho == '3':

    elif uuucho == '4':

    elif uuucho == '5':

    elif uuucho == '6':

    elif uuucho == '0':

    else:
        print('不存在此编号！重新输入！')
        time.sleep(1)
