print("hello to quiz")
print("one piece is trash :")
r = ["1/ yes", "2/ non", "3/ trash"]
print("Voici la liste des reponce ")
print(*r, sep = "\n")
print()
a = input("votre reponce :")
a2= "non"
a3= "trash"

if a in ('yes','1','y') :
    print("correct")
elif a in ('non','2','n') :
    print("false")
else:
    print("you are a genius")
