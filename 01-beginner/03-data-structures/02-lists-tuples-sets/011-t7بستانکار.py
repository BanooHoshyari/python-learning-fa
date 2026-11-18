transaction = [120, -50, 300, -20, 450, -100]

positive_transactions = list(
    filter(lambda amount: amount > 0, transaction)
)

print(positive_transactions)