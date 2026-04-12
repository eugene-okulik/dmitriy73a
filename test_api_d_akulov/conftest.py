import pytest
from endpoints.create_obj import CreateObj
from endpoints.put_obj import PutObj
from endpoints.patch_obj import PatchObj
from endpoints.delete_obj import DeleteObj


@pytest.fixture()
def create_obj_fixture():
    obj = CreateObj()
    yield obj
    if obj.js and "id" in obj.js:
        obj.delete_obj()


@pytest.fixture()
def put_obj_fixture():
    obj = PutObj()
    obj.create_new_obj()
    yield obj
    if obj.js and "id" in obj.js:
        obj.delete_obj()


@pytest.fixture()
def patch_obj_fixture():
    obj = PatchObj()
    obj.create_new_obj()
    yield obj
    if obj.js and "id" in obj.js:
        obj.delete_obj()


@pytest.fixture()
def delete_obj_fixture():
    obj = DeleteObj()
    obj.create_new_obj()
    return obj
