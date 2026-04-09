import requests
import pytest
import allure


@allure.feature("use create_and_delete_fixture")
def test_one_object(func_message, session_message, create_and_delete_fixture):
    req = requests.get(f"http://objapi.course.qa-practice.com/object/{create_and_delete_fixture.json()['id']}")
    assert req.json()["id"] == create_and_delete_fixture.json()["id"]


@pytest.mark.skip("просто скипаем для теста")
@allure.story("что-то и за чем то")
def test_test(func_message):
    print("тестируем скип")
    pass


@allure.feature("parametrize")
@allure.story("что-то и за чем то")
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
    requests.delete(f"http://objapi.course.qa-practice.com/object/{new_post.json()['id']}")


@allure.feature("use create_and_delete_fixture")
@pytest.mark.critical
def test_put(func_message, create_and_delete_fixture):
    obj = requests.put(f"http://objapi.course.qa-practice.com/object/{create_and_delete_fixture.json()['id']}",
                       json={'data': {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'}, 'name': 'test777'})
    assert obj.status_code == 200, "неверный статус код"
    assert type(obj.json()["name"]) == str, "поле name содержит не str"
    assert type(obj.json()["data"]) == dict, "поле data содержит не dict"
    assert obj.json()["name"] == "test777", "поле name содержит не те данные что отправили"
    assert obj.json()["data"] == {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'}, \
        "поле data содержит не те данные что отправили"
    assert type(obj.json()['id']) == int, "поле id содержит не int"


@allure.feature("use create_and_delete_fixture")
@pytest.mark.medium
def test_patch(func_message, create_and_delete_fixture):
    obj = requests.patch(f"http://objapi.course.qa-practice.com/object/{create_and_delete_fixture.json()['id']}",
                         json={'name': 'test888'})
    assert obj.status_code == 200, "неверный статус код"
    assert type(obj.json()["name"]) == str, "поле name содержит не str"
    assert type(obj.json()["data"]) == dict, "поле data содержит не dict"
    assert type(obj.json()["id"]) == int, "поле id содержит не int"
    assert obj.json()["name"] == "test888", "поле name содержит не те данные что отправили"
    assert obj.json()["data"] == {'color': 'qqq', 'size': 'zxc'}, \
        "в поле data изменились данные"


@allure.title("тест проверяет удаление объекта и описывает каждый шаг")
@allure.issue("https://cdn-kz.kursiv.media/wp-content/uploads/2024/10/13-11-3.jpg", "test001")
def test_delete():
    with allure.step("create object {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'}"):
        obj = requests.post("http://objapi.course.qa-practice.com/object",
                            json={'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'})
    with allure.step(f"delete object id {obj.json()['id']}"):
        delete_obj = requests.delete(f"http://objapi.course.qa-practice.com/object/{obj.json()['id']}")
    with allure.step(f"deleting again object id {obj.json()['id']}"):
        delete_obj_2 = requests.delete(f"http://objapi.course.qa-practice.com/object/{obj.json()['id']}")
    with allure.step("check responce code is 200"):
        assert delete_obj.status_code == 200, "неверный статус код"
    with allure.step("check responce text"):
        assert delete_obj.text == f"Object with id {obj.json()['id']} successfully deleted"
    with allure.step("check responce code is 404 deleting again object"):
        assert delete_obj_2.status_code == 404, "неверный статус код при повторном удалении"

# скрины
# https://disk.yandex.ru/i/ItMLSLjYQZ2jiQ
# https://disk.yandex.ru/i/mp3a5IGB6mm-Vg
