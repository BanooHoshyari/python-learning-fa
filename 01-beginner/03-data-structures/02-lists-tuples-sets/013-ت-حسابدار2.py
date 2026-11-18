documents = [
    (1001, "posted"),
    (1002, "draft"),
    (1003, "posted"),
    (1004, "rejected"),
    (1005, "draft"),
]

draft_documents = list(
    filter(lambda document: document[1] == "draft", documents)
)

print(draft_documents)