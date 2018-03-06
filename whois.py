import pyautogui as pgi
pgi.PAUSE = 0.5
pgi.FAILSAFE = True

pgi.click(114,1063)
pgi.hotkey('ctrl','t')
pgi.hotkey('ctrl','l')
pgi.typewrite('centralops.net')
pgi.hotkey('enter')
