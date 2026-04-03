import requests
from colorama import init, Fore

init(autoreset=True)


def all_objects():
    return requests.get("http://objapi.course.qa-practice.com/object")


def one_object(obj):
    return requests.get("http://objapi.course.qa-practice.com/object/%s" % obj)


def post_object():
    return requests.post("http://objapi.course.qa-practice.com/object",
                         json={'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'})


def put_object(obj):
    return requests.put("http://objapi.course.qa-practice.com/object/%s" % obj,
                        json={'data': {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'}, 'name': 'test777'})


def patch_object(obj):
    return requests.patch("http://objapi.course.qa-practice.com/object/%s" % obj,
                          json={'name': 'test888'})


def delete_object(obj):
    return requests.delete("http://objapi.course.qa-practice.com/object/%s" % obj)


def post_test():
    obj = post_object()
    try:
        assert obj.status_code == 200, "неверный статус код"
        assert type(obj.json()["name"]) == str, "поле name содержит не str"
        assert type(obj.json()["data"]) == dict, "поле data содержит не dict"
        assert type(obj.json()["id"]) == int, "поле id содержит не int"
        assert obj.json()["name"] == "test666", "поле name содержит не те данные что отправили"
        assert obj.json()["data"] == {'color': 'qqq', 'size': 'zxc'}, "поле data содержит не те данные что отправили"
    except AssertionError as e:
        print(Fore.RED + "В функции post_test, тестируем метод post, ошибка", e)
    delete_object(obj.json()["id"])


def put_test():
    obj = post_object()
    put_obj = put_object(obj.json()["id"])
    try:
        assert put_obj.status_code == 200, "неверный статус код"
        assert type(put_obj.json()["name"]) == str, "поле name содержит не str"
        assert type(put_obj.json()["data"]) == dict, "поле data содержит не dict"
        assert put_obj.json()["name"] == "test777", "поле name содержит не те данные что отправили"
        assert put_obj.json()["data"] == {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'}, \
            "поле data содержит не те данные что отправили"
        assert type(put_obj.json()["id"]) == int, "поле id содержит не int"
    except AssertionError as e:
        print(Fore.RED + "В функции put_test, тестируем метод put, ошибка", e)
    delete_object(put_obj.json()["id"])


def patch_test():
    obj = post_object()
    patch_obj = patch_object(obj.json()["id"])
    try:
        assert patch_obj.status_code == 200, "неверный статус код"
        assert type(patch_obj.json()["name"]) == str, "поле name содержит не str"
        assert type(patch_obj.json()["data"]) == dict, "поле data содержит не dict"
        assert type(patch_obj.json()["id"]) == int, "поле id содержит не int"
        assert patch_obj.json()["name"] == "test888", "поле name содержит не те данные что отправили"
        assert patch_obj.json()["data"] == {'color': 'qqq', 'size': 'zxc'}, \
            "в поле data изменились данные"
    except AssertionError as e:
        print(Fore.RED + "В функции patch_test, тестируем метод patch, ошибка", e)
    delete_object(patch_obj.json()["id"])


def delete_test():
    obj = post_object()
    delete_obj = delete_object(obj.json()["id"])
    delete_obj_2 = delete_object(obj.json()["id"])
    try:
        assert delete_obj.status_code == 200, "неверный статус код"
        assert delete_obj.text == "Object with id %s successfully deleted" % obj.json()["id"]
        assert delete_obj_2.status_code == 404, "неверный статус код при повторном удалении"
    except AssertionError as e:
        print(Fore.RED + "В функции delete_test, тестируем метод delete, ошибка", e)


post_test()
put_test()
patch_test()
delete_test()
