coke_price = 50
coin_accepted = [25,10,5]
while(coke_price > 0):
    print("Amount Due: "+str(coke_price))
    while True:
        coin_inserted = int(input("Insert Coin: "))
        if(coin_inserted not in coin_accepted):
            print("Amount Due: "+str(coke_price))
            continue
        else:
            break
    coke_price -= coin_inserted
print("Change Owed: "+ str(coke_price*-1))