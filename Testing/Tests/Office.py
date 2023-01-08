class employer():

    def __init__(self, name, uname, salary):
        self.name = name
        self.uname = uname
        self.salary = salary

    def getRaise(self, Raise=5000):
        self.salary += Raise

    def employer_info(self):
        print("Name: " + self.name.title() + ' ' + self.uname.title())
        print("Salary: " + str(self.salary))

