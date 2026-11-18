descriptions = [
    "   salarY payment ",
    "Purchase of supplies  ",
    " rent ExpenSe  ",
]

clean_descriptions = list(
    map(lambda description: description.strip().upper(), descriptions)
)

print(clean_descriptions)