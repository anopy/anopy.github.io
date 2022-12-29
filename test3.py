name_to_full_yuansuchongneng ={'迪卢克':'3','凯亚':'2','砂糖':'2'}     # 定义字典，把角色名称与元素充能最大数相联系
id_to_full_yuansuchongneng = {'000001':'3','000002':'2','000003':'3'}   # 定义字典，把角色id与元素充能最大数相联系
id_to_basic_attack_blood = {'000001':'2','000002':'2','000003':'1'}     # 把角色id与普通攻击扣除血量联系起来
id_to_basic_attack_yuansu = {'000001':'','000002':'','000003':'风'}      # 把id与普通攻击附着的元素联系起来
id_to_basic_attack_zhiding_shaiziname = {'000001':'火','000002':'冰','000003':'风'}        # 把id和普通攻击消耗的本身指定元素骰子数量联系起来
id_to_basic_attack_wuse_shaizi_num = {'000001':'2','0000002':'2','000003':'2'}          # id与普通攻击消耗无色元素数量联系
id_to_yuansu_attack_blood = {'000001':'3','000002':'3','000003':'3'}                    # id与e技能攻击伤害联系起来
id_to_yuansu_attack_zhiding_shaiziname = {'000001':'火','000002':'冰','000003':'风'}       # id与e技能攻击所需要的骰子种类联系
id_to_yuansu_attack_zhiding_shaizi_num = {'000001':'3','0000002':'3','000003':'3'}      # id与e技能攻击所需要的指定元素骰子数量联系
character_id_to_name_dir = {'000001': '迪卢克',
                            '000002': '凯亚',
                            '000003': '砂糖'}  # 共享字典，存储所有的ID对角色名称，后期改为卡ID
name_to_character_id_dir = {'迪卢克': '000001',
                            '凯亚': '000002',
                            '砂糖': '000003'}  # 共享字典，存储所有的ID对角色名称，后期改为卡ID
A_main_character = character_id_to_name_dir['000003']
A_main_cha_id = name_to_character_id_dir[A_main_character]
print(A_main_cha_id)