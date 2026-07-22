import pyautogui
import time
from ...functions import functions_ark as ark
import os

ark.log_it(f'Started {os.path.basename(__file__)}')

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.resource_menu()
ark.action_start('Arknights', 1242, 812, 339, 164)

# aketon
# ark.drag_from_to(1057, 922, 1057, 306)
# time.sleep(1)
# pyautogui.click(x=1467, y=819)
# time.sleep(1)
# ark.drag_from_to(1195, 865, 1195, 485)
# time.sleep(1)
# pyautogui.click(x=1324, y=735)
# #coag nod
# time.sleep(10)
# pyautogui.click(x=1104, y=547)

# fuscous fiber
#pyautogui.click(x=1366, y=711)
#time.sleep(1)
#pyautogui.click(x=1221, y=846)

# polyest
# pyautogui.click(x=897, y=886)
# time.sleep(1)
# ark.drag_from_to(1143, 857, 1090, 589)
# time.sleep(1)
# pyautogui.click(x=1318, y=857)
# time.sleep(1)

# orirock
# pyautogui.click(x=993, y=889)
# time.sleep(1)
# ark.drag_from_to(727, 867, 727, 623)
# pyautogui.click(x=850, y=880)

# rma
# ark.drag_from_to(1057, 922, 1057, 506)
# time.sleep(0.5)
# pyautogui.click(x=1468, y=669)
# time.sleep(0.5)
# ark.drag_from_to(1216, 882, 1216, 605)
# time.sleep(0.5)
# pyautogui.click(x=1328, y=756)

# device
# ark.drag_from_to(1057, 922, 1057, 506)
# time.sleep(0.5)
# pyautogui.click(x=1275, y=839)
# time.sleep(0.5)
# ark.drag_from_to(1027, 842, 1010, 568)
# time.sleep(0.5)
# pyautogui.click(x=1134, y=846)

# sugar
# pyautogui.click(x=1476, y=889)
# ark.drag_from_to(1196, 884, 1196, 556)
# pyautogui.click(x=1328, y=810)

# manga
# ark.drag_from_to(1057, 922, 1057, 506)
# ark.drag_from_to(1057, 922, 1057, 506)
# pyautogui.click(x=1279, y=791)
# time.sleep(0.5)
# pyautogui.click(x=1130, y=843)

# grind
# ark.drag_from_to(1057, 922, 1057, 506)
# pyautogui.click(x=1372, y=845)
# time.sleep(0.5)
# pyautogui.click(x=1226, y=843)

# cryst
# ark.drag_from_to(1057, 922, 1057, 506)
# pyautogui.click(x=808, y=834)
# time.sleep(0.5)
# ark.drag_from_to(1095, 855, 1095, 557)
# time.sleep(0.5)
# pyautogui.click(x=1225, y=732)

# oriron
# ark.drag_from_to(1057, 922, 1057, 506)
# ark.drag_from_to(1057, 922, 1057, 506)
# pyautogui.click(x=804, y=615)
# time.sleep(0.5)
# ark.drag_from_to(1084, 863, 1084, 595)
# time.sleep(0.5)
# pyautogui.click(x=1223, y=856)

# gel
ark.drag_from_to(1057, 922, 1057, 506)
pyautogui.click(x=994, y=671)
time.sleep(0.5)
ark.drag_from_to(725, 855, 718, 608)
time.sleep(0.5)
pyautogui.click(x=848, y=767)


time.sleep(20)
ark.action_start('Arknights', 1242, 812, 339, 164)
pyautogui.click(x=1307, y=859)
time.sleep(1)
pyautogui.click(x=1307, y=553)
time.sleep(1)

ark.start_farm()
time.sleep(250)

ark.action_start('Arknights', 1242, 812, 339, 164)
ark.big_out()

ark.log_it(f'Ended {os.path.basename(__file__)}')