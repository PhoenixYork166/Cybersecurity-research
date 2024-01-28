import random, pyautogui as pyauto
for i in range(15):
    height = random.randint(0, 1080)
    width = random.randint(0, 1920)
    # auto click using Desktop resolution every 0.3s
    pyauto.click(height, width, duration = 0.3)
    # Making victims accidentally mouse left click all the time
    pyauto.hotkey('winleft', 'm')
