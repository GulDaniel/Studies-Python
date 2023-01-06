class User():
    def __init__(self, first_name, last_name, 
        username, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser: " + self.username.title())
        print('Fist name: ' + self.first_name.title())
        print('Last name: ' + self.last_name.title())
        print('Age: ' + str(self.age))
        print('Locaton: ' + self.location.title())
        print('Gender: ' + self.gender.title())

    def greet_user(self):
        print("Welcome " + self.username.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
