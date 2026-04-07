import requests
import pytest


@pytest.fixture()
def new_post():
    req = requests.post("http://objapi.course.qa-practice.com/object",
                        json={'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'})
    yield req
    requests.delete(f"http://objapi.course.qa-practice.com/object/{req.json()["id"]}")


@pytest.fixture(scope="session")
def session_message():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def func_message():
    print("before test")
    yield
    print("after test")


def test_one_object(func_message, session_message, new_post):
    req = requests.get(f"http://objapi.course.qa-practice.com/object/{new_post.json()["id"]}")
    assert req.json()["id"] == new_post.json()["id"]


@pytest.mark.skip("просто скипаем для теста")
def test_test(func_message):
    print("тестируем скип")
    pass


@pytest.mark.parametrize("obj", [{'data': {'color': 'q1', 'size': 'z1'}, 'name': 'test1'},
                                 {'data': {'color': 'q2', 'size': 'z2'}, 'name': 'test2'},
                                 {'data': {'color': 'q3', 'size': 'z3'}, 'name': 'test3'}])
def test_post(func_message, obj):
    new_post = requests.post("http://objapi.course.qa-practice.com/object",
                             json=obj)
    print(new_post.json())
    assert new_post.status_code == 200, "неверный статус код"
    assert type(new_post.json()["name"]) == str, "поле name содержит не str"
    assert type(new_post.json()["data"]) == dict, "поле data содержит не dict"
    assert type(new_post.json()["id"]) == int, "поле id содержит не int"
    requests.delete(f"http://objapi.course.qa-practice.com/object/{new_post.json()["id"]}")


@pytest.mark.critical
def test_put(func_message, new_post):
    obj = requests.put(f"http://objapi.course.qa-practice.com/object/{new_post.json()["id"]}",
                       json={'data': {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'}, 'name': 'test777'})
    assert obj.status_code == 200, "неверный статус код"
    assert type(obj.json()["name"]) == str, "поле name содержит не str"
    assert type(obj.json()["data"]) == dict, "поле data содержит не dict"
    assert obj.json()["name"] == "test777", "поле name содержит не те данные что отправили"
    assert obj.json()["data"] == {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'}, \
        "поле data содержит не те данные что отправили"
    assert type(obj.json()["id"]) == int, "поле id содержит не int"


@pytest.mark.medium
def test_patch(func_message, new_post):
    obj = requests.patch(f"http://objapi.course.qa-practice.com/object/{new_post.json()["id"]}",
                         json={'name': 'test888'})
    assert obj.status_code == 200, "неверный статус код"
    assert type(obj.json()["name"]) == str, "поле name содержит не str"
    assert type(obj.json()["data"]) == dict, "поле data содержит не dict"
    assert type(obj.json()["id"]) == int, "поле id содержит не int"
    assert obj.json()["name"] == "test888", "поле name содержит не те данные что отправили"
    assert obj.json()["data"] == {'color': 'qqq', 'size': 'zxc'}, \
        "в поле data изменились данные"
