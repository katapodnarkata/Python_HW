amount=int(input("Enter price: "))
if amount>20:
    print(f"price with discount: {amount-(amount*35/100)} NIS")
else:
    print("price: ",amount,"NIS")
    