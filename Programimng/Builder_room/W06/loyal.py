price = int(input())
if price >=1000:
    discount = f"Discounted price: {price - (price/10)}"
else:
    discount = "Nothing"
print(discount)