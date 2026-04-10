import pytest

NEGATIVE_DATA = [{'name': 'test1'},
                 {'data': {'color': 'qqq', 'size': 'zxc'}},
                 {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 123}]


def test_put_obj_positive(put_obj_fixture):
    put_obj_fixture.create_new_obj()
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_response_status_code()
    put_obj_fixture.delete_obj()


@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_put_obj_negative(put_obj_fixture, data):
    put_obj_fixture.create_new_obj()
    put_obj_fixture.make_changes_in_obj(data)
    put_obj_fixture.check_bad_request()
    put_obj_fixture.delete_obj()


def test_check_type_name(put_obj_fixture):
    put_obj_fixture.create_new_obj()
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_type_name()
    put_obj_fixture.delete_obj()


def test_check_type_data(put_obj_fixture):
    put_obj_fixture.create_new_obj()
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_type_data()
    put_obj_fixture.delete_obj()


def test_check_type_id(put_obj_fixture):
    put_obj_fixture.create_new_obj()
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_type_id()
    put_obj_fixture.delete_obj()


def test_check_correct_name(put_obj_fixture):
    put_obj_fixture.create_new_obj()
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_correct_name()
    put_obj_fixture.delete_obj()


def test_check_correct_data(put_obj_fixture):
    put_obj_fixture.create_new_obj()
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_correct_data()
    put_obj_fixture.delete_obj()
