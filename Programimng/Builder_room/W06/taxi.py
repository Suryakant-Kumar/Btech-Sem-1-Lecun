kms = int(input())
price = float(50)
if kms == 0:
    print("No Trip")
elif kms<=2:
    print(f"Fare: {price}")
else:
    print(f"Fare: {price + (kms - 2) * 15}")