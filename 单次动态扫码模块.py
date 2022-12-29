import time
import cv2
import pyzbar.pyzbar as pyzbar

barcodeData1 = ''

found = set()
capture = cv2.VideoCapture(1)

# 摄像头设置
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
capture.set(cv2.CAP_PROP_EXPOSURE, 0.12)

while True:
    # 读取摄像头中的图像，ok为是否读取成功的判断参数
    ret, frame = capture.read()
    # 转为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    sss = len(barcodes)
    if sss != 0:  # 若列表不为空，则截取data部分并赋值给strstt，结束扫码
        print('\r', "手牌ID：", end='')
        stt = barcodes[0]
        strstt: str = str(stt)
        idlist = strstt[15:21]
        print(idlist)
        break
    else:          # 若列表为空，则循环扫码操作，直到扫描到条码
        print('\r', '等待放入卡牌', end='')
        time.sleep(0.2)
        print('\r', '等待放入卡牌…', end='')
        time.sleep(0.2)
        print('\r', '等待放入卡牌……', end='')
    time.sleep(0.2)

allkapai = {'887283': '最好的伙伴', '123332': '单手剑'}        # 手牌字典，6位id(key)对应卡牌名称(value)


print('你打出了：', allkapai[idlist])
