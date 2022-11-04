def main():
    product_price = 750
    price = 0
    while price != product_price:
        price = float(input("donner votre price:"))
        if price < product_price:
            print("c'est petite")
        elif price > product_price:
            print("c'est grand")
        elif price == product_price:
            print("c'est juste ")
            break
        else:
            print("error")
main()






