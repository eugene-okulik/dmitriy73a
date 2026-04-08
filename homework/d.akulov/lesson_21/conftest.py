import requests
import pytest


@pytest.fixture()
def create_and_delete_fixture():
    req = requests.post("http://objapi.course.qa-practice.com/object",
                        json={'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'})
    yield req
    requests.delete(f"http://objapi.course.qa-practice.com/object/{req.json()['id']}")


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
