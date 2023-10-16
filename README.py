import time

def concentration_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, seconds = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

# 设置专注时长为 25 分钟
concentration_timer(25)
print("专注时间结束！")
