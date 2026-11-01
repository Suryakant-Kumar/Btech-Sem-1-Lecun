attempts = 5
while True:
    pin = input("Pin: ")
    attempts -=1
    if pin == "1234":
        print("Correct Pin")
        break
    if attempts == 0:
        print("Card Blocked")
        break
    else:
        print(f"Incorrect Pin, Only {attempts} attempts left")