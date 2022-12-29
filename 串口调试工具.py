

import serial
import binascii


callup_str = bytes.fromhex('00 00 00 00 00 00 00') #16进制转化为hex
print(callup_str)
data = str(binascii.b2a_hex(callup_str))[2:-1]  # 将16进制（hex）转化为字符串（data）
print(data)