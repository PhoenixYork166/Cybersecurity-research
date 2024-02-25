from locust import User, task, between

# Need several attributes for a User class to work
# task
# method


class MyUser(User):

    wait_time = between(1, 2)

    @task
    def login_url(self):
        print(f'I am logging into URL!')

