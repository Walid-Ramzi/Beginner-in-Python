from random import *
def registre():
    number_of_players = int(input("How Many players?: "))
    if (number_of_players % 2) == 0:
        for i in range(number_of_players):
            p = i+1
            player = input("please enter your name player_"+str(p)+": ")
            with open("players.txt", "a+") as file:
                file.write(player)
                file.write(":")
                file.write("\n")
                file.close()
            N = number_of_players - 1
            if N == 0:
                return player
    else :
        print("you can't play indvidial")

def carta():
    carta_numbers = "1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, " \
                    "6, 6, 6, 6, 7, 7, 7, 7, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12"
    shuffled_cards = list(map(int,carta_numbers.split(", ")))
    shuffle(shuffled_cards)
    #print(shuffled_cards)
    for i in range(40):
        carta_list = shuffled_cards[i]
        if i != 40:
            i += 1
        with open("carta.txt", "a+") as file:
            file.write(str(carta_list))
            file.write(":")
            file.close()
    with open("carta.txt", "a+") as file:
        file.write("\n")
        file.close()

    def table():
        table_cards = []
        for i in range(4):
            table_cards.append(choice(shuffled_cards))

        if table_cards[0] in (table_cards[1], table_cards[2], table_cards[3]) \
                or table_cards[1] in (table_cards[0], table_cards[2], table_cards[3]) \
                or table_cards[2] in (table_cards[1], table_cards[0], table_cards[3])\
                or table_cards[3] in (table_cards[1], table_cards[2], table_cards[0]):
            print("kanet m3awda 3awed badalha")
            return table()
        for i in range(4):
            i = 0
            if i < 3:
                table_cards = list(table_cards)
                old_card = table_cards.pop(i)
                old_card = int(old_card)
                new_cards = shuffled_cards.remove(old_card)
                print(shuffled_cards)
                i = i + 1

    table()
carta()


#def give_cards():









    #user_name = input("what is your full name please :")
    #account = input("please type your email :")
    #password = input("please type your password :")
    #with open("tests.txt", "a+") as file:
     #   file.write(player)
      #  file.write(":")
        #file.write(password)
        #file.write(" ")
        #file.write("")
        #file.close()
    #registre()
