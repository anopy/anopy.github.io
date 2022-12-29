import os
import time
import serial
import serial.tools.list_ports
import binascii

# 以下为PN532各功能16进制指令转换hex

send_wake_up_hex = bytes.fromhex('55 55 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff 03 fd d4 14 01 17 00')
send_read_id_hex = bytes.fromhex('00 00 FF 04 FC D4 4A 02 00 E0 00')

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
print('\r','好的，现在，请关闭所有开关，按任意键以配置读卡器。',end='')
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
    exit(0)
Aser1.write(send_wake_up_hex)
wkup_answer_A1 = Aser1.inWaiting()
time.sleep(0.5)
Aser1.write(send_read_id_hex)
test_answer_A1 = Aser1.inWaiting()
if test_answer_A1 is not None:
    testdata = str(binascii.b2a_hex(Aser1.read(test_answer_A1)))[2:-1]
    print('读取数据:', testdata)
else:
    print('未读到数据！请退出重试！')
    os.system('pause')
    exit(0)

print('测试完成，初始化成功')

