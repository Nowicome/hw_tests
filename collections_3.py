stats = {"facebook": 55, "yandex": 120, "vk": 115, "google": 99, "email": 42, "ok": 98}


def top_firm(row: dict):
    return max(row, key=row.get)


if __name__ == "__main__":
    print(top_firm(stats))
