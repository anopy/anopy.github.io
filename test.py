import time
for i in range(15):
    time.sleep(0.5) # 这里为了查看输出变化，实际使用不需要sleep
    print('\r', i, end='')
    # print('\r', 15-i, end='') # 从两位变一位会有问题
