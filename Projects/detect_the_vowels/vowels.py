def getting(mot):
    vol = ["a","e","i","u","o","y"]
    a=0
    for letter in mot:
        if letter in vol:
            a+=1
    return a
mot = str(input("donner votre mot:"))
a = getting(mot)
print(getting(mot))
