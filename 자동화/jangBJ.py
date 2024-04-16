import pyautogui
import time
import clipboard


# time.sleep(1)
# post_text = (1282, 566)
# print(post_text)

# time.sleep(2)
# send_text = (1385, 643)
# print(send_text)



tx, ty = 1282, 566
sx, sy = 1385, 643



def sendMessage(str, sec):
    #clipboard.copy(str)
    pyautogui.moveTo(tx, ty, duration=1)
    pyautogui.click()
    pyautogui.write(str)
    #pyautogui.hotkey('command', 'v')
    pyautogui.moveTo(sx, sy)
    pyautogui.click()
    time.sleep(sec)
    

sendMessage("wkdqudwkd", 1)
sendMessage('zz', 2)
