def calculate_VAT(price, vat_rate):
    return price * (100 + vat_rate)/100

order_price = [100, 140, 400]

for price in order_price:
    final_amount = calculate_VAT(price, 10)
    print(f"Original amount is: {price}, Amount after VAT is: {final_amount}")