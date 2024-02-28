from locust import HttpUser, task, between

# Need several attributes for a User class to work
# task
# method


class MyUser(HttpUser):

    wait_time = between(1, 2)
    host = 'http://192.168.2.65:8082'
    
    # Can define host by
    # python -m locust -f basic_http_host01.py --host="http://newtours.demoaut.com"

    @task
    def login_url(self):
        print(f'I am logging into URL!')

