tax_rates = [0.09, -0.05, 0, 0.10, "invalid", 0.25, None, 0.09]

valid_rates = list(
    filter(lambda rate: isinstance(rate, (int, float)) and rate > 0, tax_rates)
)

print(valid_rates)
