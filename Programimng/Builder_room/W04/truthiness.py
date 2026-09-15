print(bool(0), bool(0.0), bool(""), bool(None)) # empty things are falsy value in python
print(bool(5), bool("hi"), bool(-1)) # non empty things are truthy value in python
# x = int(input("Enter a value: "))
if "Surya":
    print("Hello")
if "":
    print("Falsy value in if statement")
print(0 or 5)
print(0 or 0.0 or 5.9 or "Hello")
print("" or "hi")
print(3 and 7)
print(0 and 7)