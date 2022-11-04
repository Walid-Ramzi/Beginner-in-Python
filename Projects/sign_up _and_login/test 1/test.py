from register import *
from loggin import *
account = None
regaccount = None
def main():
    account = None
    regaccount = None
    print("hello user welcome to are site what you want to Do ")
    print("1/ register", "\n" "2/ loggin")
    choice = input("type your answer here :")
    if choice in ("register", "1"):
        account = register(input("Email :").split("/"), input("Username :").split("/"), input("Password :").split("/"))
        liste1 = list(account.email)
        from copy import deepcopy
        liste2 = list(account.username)
        liste3 = list(account.password).copy()
        copied_list = liste3
        from copy import copy
        copy(liste3)
        while True:
            main()
            break


    elif choice in ("loggin", "2"):
        regacccount = loggin(input("Email or Username :").split("/"), input("Password :").split("/"))
        regliste1 = list(regacccount.user)
        regliste2 = list(regacccount.passw)

        from copyreg import pickle
        from copy import copy
        print()

        if regliste2 == liste3 :
            print("you are right")
        else:
            print("ba3")

main()









