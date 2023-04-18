import requests
import unittest


# ficture , factoryboy
#  созд
class TestApp(unittest.TestCase):

    def setUp(self):
        self.port = 8000
        self.id = 1
        self.data = {
            "name": "Misha",
            "email": "misha@mail.ru",
            "phone": 79991234567
        }

        self.data2 = {
            "name": "Dima",
            "email": "dima@mail.ru",
            "phone": 79991234567
        }

        self.data3 = {
            "name": "Tima",
            "email": "dima@mail.ru",
            "phone": 79991234567
        }

    # def tearDown(self):
    #     self.widget.dispose()

    def test_1_post(self):
        res = requests.post(f"http://127.0.0.1:{self.port}/", json=self.data)
        id = res.json().get('id')
        name = res.json().get('name')
        print(res)
        self.assertEqual(id, 1)
        self.assertEqual(name, 'Misha')
        self.assertEqual(res.status_code, 201)

    def test_2_put(self):
        res = requests.put(f"http://127.0.0.1:{self.port}/{self.id}", json=self.data2)
        # name = res.name
        # self.assertEqual(name,'saule')
        # print(res)
        self.assertEqual(res.status_code, 204)

    def test_3_get(self):
        res = requests.get(f"http://127.0.0.1:{self.port}/{self.id}")
        name = res.json().get('name')
        self.assertEqual(name, 'Dima')
        self.assertEqual(res.status_code, 200)

    def test_4_delete(self):
        res = requests.delete(f"http://127.0.0.1:{self.port}/{self.id}")
        self.assertEqual(res.status_code, 204)


if __name__ == '__main__':
    unittest.main()