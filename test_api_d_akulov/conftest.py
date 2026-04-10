import pytest
from endpoints.create_obj import CreateObj
from endpoints.put_obj import PutObj
from endpoints.patch_obj import PatchObj
from endpoints.delete_obj import DeleteObj


@pytest.fixture()
def create_obj_fixture():
    return CreateObj()


@pytest.fixture()
def put_obj_fixture():
    return PutObj()


@pytest.fixture()
def patch_obj_fixture():
    return PatchObj()


@pytest.fixture()
def delete_obj_fixture():
    return DeleteObj()
