ids = {
    "user1": [213, 213, 213, 15, 213],
    "user2": [54, 54, 119, 119, 119],
    "user3": [213, 98, 98, 35]
}


def sort_unique_row(row: dict):
    unique_row = set()
    for key, val in row.items():
        unique_row |= set(val)
    return sorted(unique_row)


if __name__ == "__main__":
    print(sort_unique_row(ids))
