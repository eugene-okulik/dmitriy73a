import pytest

NEGATIVE_DATA = [{'name': 'test1'},
                 {'data': {'color': 'qqq', 'size': 'zxc'}},
                 {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 123}]


def test_create_obj_positive(create_obj_fixture):
    body_in_test = {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test1'}
    create_obj_fixture.create_new_obj(body_in_test)
    create_obj_fixture.check_response_status_code()
    create_obj_fixture.delete_obj()


@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_create_object_negative(create_obj_fixture, data):
    create_obj_fixture.create_new_obj(data)
    create_obj_fixture.check_bad_request()


def test_check_type_name(create_obj_fixture):
    create_obj_fixture.create_new_obj()
    create_obj_fixture.check_type_name()
    create_obj_fixture.delete_obj()


def test_check_type_data(create_obj_fixture):
    create_obj_fixture.create_new_obj()
    create_obj_fixture.check_type_data()
    create_obj_fixture.delete_obj()


def test_check_type_id(create_obj_fixture):
    create_obj_fixture.create_new_obj()
    create_obj_fixture.check_type_id()
    create_obj_fixture.delete_obj()
