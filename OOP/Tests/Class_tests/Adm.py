from Users import User

class Privilegies():
    def __init__(self, privilegies=["can add post", "can undelete post",
            "can ban user", "can remove post", "can unban user"]):
        self.privilegies = privilegies

    def show_privilegies(self):
        print("This user has those privilegies as Admin:")
        for privilegie in self.privilegies:
            print("- " + privilegie)

class Admin(User):
    def __init__(self, first_name, last_name,
        username, age, location, gender):
        super().__init__(first_name, last_name, 
            username, age, location, gender)
        self.privilegies = Privilegies()
