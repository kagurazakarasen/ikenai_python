# 自動スクリーンキャプチャ＆ページめくり
# 繰り返し数を適当にセット。終了はCTRL+C
# Macでしか試していない。

import pyautogui
import sys
import time

time.sleep(5)   # 画面変更用に５秒待つ。MacならCommand+Tabぽち
print('ScreenShot Start!')

i=0

while i<130:    # 繰り返す数。大体200pぐらいなら見開きで100回。
    s = 'ss{:0=3}.png'.format(i)
    time.sleep(.5)  # 0.5秒待つ。要調整
    #pyautogui.screenshot('my_screenshot.png')
    pyautogui.screenshot(s)
    print(s)
    i += 1
    pyautogui.press('left')   # 左矢印で行けるばあい（ebo〇k jap〇n等
    #pyautogui.click(50,400)    # 画面左側でクリックするばあい（ｘ、ｙは適当）


