class User:
    def __init__(self,first_name,last_name):
        self.firstname = first_name
        self.lastname = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"用户的名字是{self.firstname}{self.lastname}")
        
    def greet_user(self):
        print(f"尊敬的{self.firstname}先生，您好！")
              