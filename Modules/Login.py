def make_login(username):
    """Ask user to input his password 3 times"""
    print("Hello, " + username + ".")
    pssw = 123    
    chances = 3
    while chances > 0:
        password = int(input("What is your password?: "))
        if password == pssw:
            print("Logging into " + username + " account...")
            break
        else:
            chances -= 1
            if chances > 0:            
                print("Incorrect password!" +
                    " You still has " + str(chances) + " chances.")
            else:
                print("Incorret password! No more chances!")                
                print("You'll have to wait a few minutes to try again.")
