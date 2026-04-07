import requests
import unittest
import sys


# оставлю для себя шпаргалку на всякий случай))

class TestApi(unittest.TestCase):

    # предусловие, создаем пользователя
    def setUp(self):
        self.post = requests.post("http://objapi.course.qa-practice.com/object",
                                  json={'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'})
        print(f'\nPost created: {self.post.json()["id"]}')

    # постусловие, удаляем пользователя
    def tearDown(self):
        requests.delete(f"http://objapi.course.qa-practice.com/object/{self.post.json()["id"]}")
        print(f'Post deleted: {self.post.json()["id"]}')

    def test_post(self):
        self.assertEqual(self.post.status_code, 200)
        self.assertEqual(type(self.post.json()["name"]), str)
        self.assertEqual(type(self.post.json()["data"]), dict)
        self.assertEqual(type(self.post.json()["id"]), int)
        self.assertEqual(self.post.json()["name"], "test666")
        self.assertEqual(self.post.json()["data"], {'color': 'qqq', 'size': 'zxc'})


# тесты которым не нужно предусловие/постусловие выносим в отдельный класс
class TestIndependent(unittest.TestCase):
    def test_all_objects(self):
        rec = requests.get("http://objapi.course.qa-practice.com/object")
        self.assertEqual(rec.status_code, 200)

    @unittest.skip("просто пропускаем тест")
    def test_one_object(self):
        rec = requests.get("http://objapi.course.qa-practice.com/object/1")
        self.assertEqual(rec.json()["id"], 1)

    @unittest.skipIf(sys.platform == "win32", "не запускаем по условию")
    def test_1(self):
        print(sys.platform)
        pass
