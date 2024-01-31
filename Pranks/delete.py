import os

try:
    os.system("DEL H /F/Q/S*.*")
except:
    print('Could NOT delete...')