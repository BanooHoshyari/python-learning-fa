account_id = [5, 42, 108, 9, 1205, 11111]

standard_ids = list(
    map(lambda account: str(account).zfill(5), account_id)
)

print(standard_ids)