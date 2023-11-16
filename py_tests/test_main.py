import pytest
from collections_1 import strange_row
from collections_2 import sort_unique_row
from collections_3 import top_firm
import unittest
from Ya_Disk import YandexDisk


@pytest.mark.parametrize(
    "inp_list, expected", [
        (["2018-01-01", "yandex", "cpc", 100, 99], {"2018-01-01": {"yandex": {"cpc": {100: 99}}}}),
        ([23, "sorrow", 16, 32, "strange"], {23: {"sorrow": {16: {32: "strange"}}}})
    ]
)
def coll_1_test(inp_list, expected):
    res = strange_row(inp_list)
    assert res == expected


@pytest.mark.parametrize(
    "inp_dict", "expected", [
        (
                {
                    "user1": [213, 213, 213, 15, 213],
                    "user2": [54, 54, 119, 119, 119],
                    "user3": [213, 98, 98, 35]
                },
                [15, 35, 54, 98, 119, 213]),
        (
                {
                    "user1": [13, 23, 13, 5, 23],
                    "user2": [5, 4, 9, 11, 9],
                    "user3": [23, 8, 9, 3],
                    "user4": [1, 13, 8, 5],
                    "user5": [1, 5, 206, 351]
                },
                [1, 3, 4, 5, 8, 9, 11, 13, 23, 206, 351])
    ]
)
def coll_2_test(inp_dict, expected):
    res = sort_unique_row(inp_dict)
    assert res == expected


@pytest.mark.parametrize(
    "inp_dict", "expected", [
        ({"facebook": 55, "yandex": 120, "vk": 115, "google": 99, "email": 42, "ok": 98}, "yandex"),
        ({"chigo": 11, "sanyo": 26, "sharp": 42, "polaris": 23, "gree": 56, "elenberg": 13}, "gree")
    ]
)
def coll_3_test(inp_dict, expected):
    res = top_firm(inp_dict)
    assert res == expected


class TestYandexDisk(unittest.TestCase):
    def setUp(self):
        self.yad = YandexDisk()

    def test_crt_folder(self, path="new"):
        response = self.yad.create_folder(path)
        self.assertEqual(response, 200)
        self.assertEqual(response, 400)
        self.assertEqual(response, 401)
        self.assertEqual(response, 403)
        self.assertEqual(response, 404)
        self.assertEqual(response, 406)
        self.assertEqual(response, 413)
        self.assertEqual(response, 423)
        self.assertEqual(response, 429)
        self.assertEqual(response, 503)


if __name__ == "__main__":
    unittest.main()
