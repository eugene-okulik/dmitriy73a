import pytest
import requests

from endpoints.create_obj import CreateObj
from endpoints.put_obj import PutObj
from endpoints.patch_obj import PatchObj
from endpoints.delete_obj import DeleteObj


@pytest.fixture()
def post_obj_fixture():
    obj = CreateObj()
    yield obj
    if obj.js and "id" in obj.js:
        requests.delete(f"http://objapi.course.qa-practice.com/object/{obj.js['id']}")


@pytest.fixture()
def put_obj_fixture():
    return PutObj()


@pytest.fixture()
def patch_obj_fixture():
    return PatchObj()


@pytest.fixture()
def delete_obj_fixture():
    return DeleteObj()


@pytest.fixture()
def create_obj_fixture_id(post_obj_fixture, delete_obj_fixture):
    post_obj_fixture.create_new_obj()
    json_item_id = post_obj_fixture.js['id']
    yield json_item_id
    delete_obj_fixture.delete_obj(json_item_id)
