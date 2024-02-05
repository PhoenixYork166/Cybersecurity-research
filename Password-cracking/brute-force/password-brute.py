import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'\",<.>/?"

# Converting chars into a list['', '', ..., '']
allchar = list(chars)
#print(f'allchar: {allchar}')

pwd = pyautogui.password('Enter a password: ')

sample_pwd = ''

# Run as long as pwd != sample_pwd
while(sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))
    print('<-----' + str(sample_pwd) + '------>')
    
    # When matched
    if(sample_pwd == list(pwd)):
        print('The password is: ' + "".join(sample_pwd))
        # Break the inifinite loop
        break