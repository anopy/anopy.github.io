import binascii
import serial.tools

test_answer_A1 = bytes.fromhex('55 55 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff 03 fd d4 14 01 17 00')
testdata = str(binascii.b2a_hex(test_answer_A1))[2:-1]
print(test_answer_A1)
print(testdata)


