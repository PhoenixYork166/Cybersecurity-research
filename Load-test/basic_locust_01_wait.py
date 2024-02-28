from locust import User, task, between
from colorama import Fore, Back, Style
#from datetime import datetime
import time


# Get time
def getTime():
    
    try:
        
        # Get current local time as a struct time OBJ
        current_time = time.localtime()
        formatted_time = time.strftime('%Y-%m-%d-%H:%M:%S', current_time)
        
        return formatted_time
    
    except Exception as e:
        
        print(Fore.RED + f'Failed to retrieve current time :(\n')

# Retreiving current formatted time from getTime()
formatted_time = getTime()


# Need several attributes for a User class to work
# task
# method
class MyUser(User):

    wait_time = between(1, 3)

    @task
    def login_url(self):
        print(f'I am logging into URL! at {formatted_time}')
        #print(f'{datetime.now}')
