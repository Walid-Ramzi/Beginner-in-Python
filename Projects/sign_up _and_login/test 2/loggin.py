def reg():
    account = input("please type your email :")
    password = input("please type your password :")
    with open("tests.txt", "a+") as file:
        file.write(account)
        file.write(":")
        file.write(password)
        file.write(" ")
        file.write("")
        file.close()

def loggin():
    regacccount = input("please type your email :")
    passw = input("please type your password :")
    for i in open("tests.txt", "r+").readlines():
        a = i.split(":")
        print(a)

        if regacccount == a[0] and passw == a[1]:
            print("suc")
            return True
    print("ba3")
    return False


def main():
    print("hello user welcome to are site what you want to Do ")
    print("1/ register", "\n" "2/ loggin")
    choice = input("type your answer here :")
    if choice in ("register", "1"):
        return reg()
    elif choice in ("loggin", "2"):
        return loggin()
while True:
    main()