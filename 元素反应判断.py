Ayuansu1_list = []
a = input('测试元素A')  # 仅供测试使用
b = input('测试元素B')  # 仅供测试使用
Ayuansu1_list.append(a)
Ayuansu1_list.append(b)
huanchongcao = Ayuansu1_list
if '风' in huanchongcao and '水' in huanchongcao:
    Acha_situation = '扩散'
    Ayuansu1_list.clear()
elif Ayuansu1_list.count('风') == 2:
    Ayuansu1_list.clear()
    Ayuansu1_list.append('风')
    Acha_situation = ''
elif Ayuansu1_list.count('火') == 2:
    Ayuansu1_list.clear()
    Ayuansu1_list.append('火')
    Acha_situation = ''
elif Ayuansu1_list.count('雷') == 2:
    Ayuansu1_list.clear()
    Ayuansu1_list.append('雷')
    Acha_situation = ''
elif Ayuansu1_list.count('冰') == 2:
    Ayuansu1_list.clear()
    Ayuansu1_list.append('冰')
    Acha_situation = ''
elif Ayuansu1_list.count('草') == 2:
    Ayuansu1_list.clear()
    Ayuansu1_list.append('草')
    Acha_situation = ''
elif Ayuansu1_list.count('水') == 2:
    Ayuansu1_list.clear()
    Ayuansu1_list.append('水')
    Acha_situation = ''
elif Ayuansu1_list.count('岩') == 2:
    Ayuansu1_list.clear()
    Ayuansu1_list.append('岩')
    Acha_situation = ''
elif '风' in huanchongcao and '冰' in huanchongcao:
    Acha_situation = '扩散'
    Ayuansu1_list.clear()
elif '风' in huanchongcao and '火' in huanchongcao:
    Acha_situation = '扩散'
    Ayuansu1_list.clear()
elif '风' in huanchongcao and '雷' in huanchongcao:
    Acha_situation = '扩散'
    Ayuansu1_list.clear()
elif '冰' in huanchongcao and '水' in huanchongcao:
    Acha_situation = '冻结'
    Ayuansu1_list.clear()
elif '火' in huanchongcao and '水' in huanchongcao:
    Acha_situation = '蒸发'
    Ayuansu1_list.clear()
elif '火' in huanchongcao and '冰' in huanchongcao:
    Acha_situation = '融化'
    Ayuansu1_list.clear()
elif '雷' in huanchongcao and '冰' in huanchongcao:
    Acha_situation = '超导'
    Ayuansu1_list.clear()
elif '雷' in huanchongcao and '水' in huanchongcao:
    Acha_situation = '导电'
    Ayuansu1_list.clear()
elif '雷' in huanchongcao and '火' in huanchongcao:
    Acha_situation = '超载'
    Ayuansu1_list.clear()
elif '岩' in huanchongcao and '火' in huanchongcao:
    Acha_situation = '结晶'
    Ayuansu1_list.clear()
elif '岩' in huanchongcao and '水' in huanchongcao:
    Acha_situation = '结晶'
    Ayuansu1_list.clear()
elif '岩' in huanchongcao and '雷' in huanchongcao:
    Acha_situation = '结晶'
    Ayuansu1_list.clear()
elif '岩' in huanchongcao and '冰' in huanchongcao:
    Acha_situation = '结晶'
    Ayuansu1_list.clear()
elif '草' in huanchongcao and '火' in huanchongcao:
    Acha_situation = '燃烧'
    Ayuansu1_list.clear()
elif '草' in huanchongcao and '水' in huanchongcao:
    Acha_situation = '绽放'
    Ayuansu1_list.clear()
elif '草' in huanchongcao and '雷' in huanchongcao:
    Acha_situation = '绽放'
    Ayuansu1_list.clear()
elif '冰' in huanchongcao and '草' in huanchongcao:
    print('两元素共存，不反应，最后附着元素为：', b)
    Acha_situation = '冰草共存中', b
    Ayuansu1_list.clear()
    Ayuansu1_list.append(b)
else:
    Acha_situation = ''
print(Acha_situation)
print(Ayuansu1_list)
