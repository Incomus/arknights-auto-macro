import pyautogui
import time
from ...functions import functions_ark as ark
import os
import keyboard

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
time.sleep(.6)
pyautogui.click(x=472, y=321) # open work
time.sleep(1)

ark.drag_down()

pyautogui.click(x=990, y=503)
time.sleep(1)
pyautogui.click(x=1194, y=244) # get siege
time.sleep(.6)
pyautogui.click(x=1500, y=701)
time.sleep(.6)
pyautogui.click(x=1474, y=928)
time.sleep(10)
keyboard.press_and_release('esc')
time.sleep(1)

pyautogui.click(x=472, y=321) # open work
time.sleep(1)

pyautogui.click(x=989, y=395) ## center
time.sleep(1)
pyautogui.click(x=1185, y=248)
time.sleep(.6)
pyautogui.click(x=1225, y=698)
time.sleep(.6)
pyautogui.click(x=1497, y=695)
time.sleep(1)
pyautogui.moveTo(1538, 437)
pyautogui.mouseDown()
pyautogui.moveTo(640, 453, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(.6)
pyautogui.click(x=1445, y=435)
time.sleep(.6)
pyautogui.click(x=1165, y=448)
time.sleep(.6)
pyautogui.click(x=1312, y=435)
time.sleep(.6)
pyautogui.click(x=1476, y=923)
time.sleep(10)

pyautogui.click(x=990, y=545) ## recep
time.sleep(1)
pyautogui.moveTo(1523, 435)
pyautogui.mouseDown()
pyautogui.moveTo(822, 423, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(.6)
pyautogui.click(x=1101, y=428)
time.sleep(.6)
pyautogui.click(x=1375, y=685)
time.sleep(.6)
pyautogui.click(x=1476, y=923)
time.sleep(10)

pyautogui.click(x=992, y=749) ## trade1
time.sleep(1)
pyautogui.click(x=1221, y=419)
time.sleep(.6)
pyautogui.click(x=1185, y=248)
time.sleep(.6)
pyautogui.click(x=1367, y=413)
time.sleep(.6)
count = 12
while count > 0:
    pyautogui.moveTo(1550, 387)
    pyautogui.mouseDown()
    pyautogui.moveTo(365, 387, 0.3)
    pyautogui.mouseUp()
    time.sleep(.6)
    count = count - 1
time.sleep(1)
pyautogui.click(x=1269, y=241)
time.sleep(.6)
pyautogui.click(x=1269, y=241)
time.sleep(.6)
pyautogui.click(x=1353, y=697)
time.sleep(.6)
pyautogui.click(x=1458, y=932)
time.sleep(10)

pyautogui.click(x=992, y=900) ## trade2
time.sleep(1)
pyautogui.click(x=1188, y=239)
time.sleep(.6)
pyautogui.click(x=1188, y=239)
time.sleep(.6)
pyautogui.click(x=950, y=688)
time.sleep(.6)
pyautogui.click(x=1216, y=450)
time.sleep(.6)
pyautogui.click(x=1188, y=239)
time.sleep(.6)
pyautogui.click(x=1093, y=413)
time.sleep(.6)
pyautogui.click(x=1475, y=922)
time.sleep(10)

ark.drag_down()

pyautogui.click(x=988, y=351) ## power1
time.sleep(1)
pyautogui.click(x=805, y=430)
time.sleep(.6)
pyautogui.click(x=1478, y=926)
time.sleep(10)

pyautogui.click(x=993, y=867) ## fac1 gold
time.sleep(.6)
pyautogui.click(x=1362, y=433)
time.sleep(.6)
pyautogui.moveTo(1538, 451)
pyautogui.mouseDown()
pyautogui.moveTo(935, 449, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(.6)
pyautogui.click(x=1184, y=700)
time.sleep(.6)
pyautogui.click(x=1328, y=437)
time.sleep(.6)
pyautogui.click(x=1474, y=927)
time.sleep(10)

ark.drag_down()

pyautogui.click(x=989, y=316) ## fac2 gold
time.sleep(1)
pyautogui.moveTo(1538, 451)
pyautogui.mouseDown()
pyautogui.moveTo(935, 449, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(.6)
pyautogui.click(x=1051, y=682)
time.sleep(.6)
pyautogui.click(x=1185, y=248)
time.sleep(1)
pyautogui.moveTo(1538, 451)
pyautogui.mouseDown()
pyautogui.moveTo(935, 449, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(.6)
pyautogui.click(x=1162, y=442)
time.sleep(.6)
pyautogui.click(x=1158, y=698)
time.sleep(.6)
pyautogui.click(x=1185, y=248)
time.sleep(.6)
pyautogui.click(x=1461, y=928)
time.sleep(10)

pyautogui.click(x=988, y=465) ## power2
time.sleep(1)
pyautogui.click(x=813, y=693)
time.sleep(.6)
pyautogui.click(x=1474, y=924)
time.sleep(10)

pyautogui.click(x=991, y=950) ## fac3 gold
time.sleep(1)
pyautogui.click(x=1362, y=698)
time.sleep(.6)
pyautogui.click(x=1499, y=433)
time.sleep(.6)
pyautogui.click(x=1499, y=704)
time.sleep(.6)
pyautogui.click(x=1473, y=928)
time.sleep(10)

ark.drag_down()

pyautogui.click(x=992, y=430) ## power3
time.sleep(1)
pyautogui.moveTo(1510, 419)
pyautogui.mouseDown()
pyautogui.moveTo(1048, 418, 1)
time.sleep(1)
pyautogui.mouseUp()
time.sleep(.6)
pyautogui.click(x=1333, y=433)
time.sleep(.6)
pyautogui.click(x=1476, y=923)
time.sleep(10)

pyautogui.click(x=990, y=583) ## fac4 exp
time.sleep(1)
pyautogui.click(x=1185, y=248)
time.sleep(1)
pyautogui.click(x=1492, y=434)
time.sleep(.6)
pyautogui.click(x=1225, y=701)
time.sleep(.6)
pyautogui.click(x=1082, y=687)
time.sleep(.6)
pyautogui.click(x=1473, y=928)
time.sleep(10)

keyboard.press_and_release('esc')
time.sleep(2)

ark.log_it(f'Ended {os.path.basename(__file__)}')