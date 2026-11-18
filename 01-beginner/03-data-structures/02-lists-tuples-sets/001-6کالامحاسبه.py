quantities = [10, 5, 20, 8]
unit_prices = [15000, 80000, 1200, 45000]

total_amounts = list(
    map(lambda quantity, unit_price: quantity * unit_price,
        quantities, unit_prices)
)

print(total_amounts)