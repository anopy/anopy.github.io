import os

character_id_to_name_dir = {'000001': '迪卢克',
                            '000002': '凯亚',
                            '000003': '砂糖'}  # 共享字典，存储所有的ID对角色名称，后期改为卡ID

while True:
    Acharacter1_id = str(input('A方测试角色1 ID：'))  # 后期此处为读卡识别的ID
    Acharacter2_id = str(input('A方测试角色2 ID：'))
    Acharacter3_id = str(input('A方测试角色3 ID：'))
    character_id_pool = [Acharacter1_id, Acharacter2_id, Acharacter3_id]
    if Acharacter1_id == Acharacter2_id or Acharacter1_id == Acharacter3_id or Acharacter2_id == Acharacter3_id:
        print('三个角色必须互不相同！请重新刷卡！')
    else:
        if Acharacter1_id in character_id_to_name_dir and Acharacter2_id in character_id_to_name_dir and Acharacter3_id in character_id_to_name_dir:
            break
        else:
            print('未找到该卡牌，请重新输入测试角色ID')

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
    main_cha_num = input('选择出战角色编号：')
    if main_cha_num == '1':
        main_character = Ach1
        os.system('cls')
        break
    elif main_cha_num == '2':
        main_character = Ach2
        os.system('cls')
        break
    elif main_cha_num == '3':
        main_character = Ach3
        os.system('cls')
        break
    else:
        print('不存在此角色！请重新输入！')

first = 'A'
print('行动阶段\n请', first, '方开始行动！')

Acharacter1_yuansuchongneng = 0
Acharacter2_yuansuchongneng = 0
Acharacter3_yuansuchongneng = 0
Bcharacter1_yuansuchongneng = 0
Bcharacter2_yuansuchongneng = 0
Bcharacter3_yuansuchongneng = 0

if main_cha_num == '1':
    main_character_yuansuchongneng = Acharacter1_yuansuchongneng
elif main_cha_num == '2':
    main_character_yuansuchongneng = Acharacter2_yuansuchongneng
elif main_cha_num == '3':
    main_character_yuansuchongneng = Acharacter3_yuansuchongneng

def firststage():  # 这是一级菜单
    print('----Menu----'
          '\n1.普通攻击'
          '\n2.元素战技'
          '\n3.元素爆发   当前元素充能：', main_character_yuansuchongneng, '/', '3'
          '\n4.使用手牌'
          '\n5.手牌转换元素骰子'
          '\n6.切换角色'
          '\n0.宣布回合结束')

first = 'A'

print('     ', Ach1, '           ', Ach2, '          ', Ach3, '          ''\n''     ', '[', Ach1_blood, ']',
      '         ', '[', Ach2_blood, ']', '        ', '[', Ach3_blood, ']')

if len(Ayuansu1) > 0 or len(Ayuansu2) > 0 or len(Ayuansu3) > 0:
    print('     ', Ayuansu1, '           ', Ayuansu2, '           ', Ayuansu3)

if main_character == Ach1:
    print('       出战')
elif main_character == Ach2:
    print('                        出战')
else:
    print('                                        出战')

print('\n\n\n\n')
print('请',first,'方行动')
firststage()
uuucho = input('输入行动编号：')


# 以上为A方出战角色信息输出UI
