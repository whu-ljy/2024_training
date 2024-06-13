class User:
    def __init__(self,first_name,last_name):
        self.firstname = first_name
        self.lastname = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"用户的名字是{self.firstname}{self.lastname}")
        
    def greet_user(self):
        print(f"尊敬的{self.firstname}先生，您好！")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post','can delete post','can ban user']
        
    def show_privileges(self):
        print(f"{self.privileges}")

A = Admin('刘','锦阳')
A.show_privileges()