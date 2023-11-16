LIST = ["2018-01-01", "yandex", "cpc", 100, 99]


def strange_row(row: list):
    dict_row = {row[-2]: row[-1]}
    for key in row[:-2][::-1]:
        dict_row = {key: dict_row}
    return dict_row


if __name__ == "__main__":
    print(strange_row(LIST))
