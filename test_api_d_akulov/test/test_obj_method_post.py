import pytest

NEGATIVE_DATA = [{'name': 'test1'},
                 {'data': {'color': 'qqq', 'size': 'zxc'}},
                 {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 123}]


def test_create_obj_positive_check_type_name_date_id(post_obj_fixture):
    body_in_test = {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test1'}
    post_obj_fixture.create_new_obj(body_in_test)
    post_obj_fixture.check_response_status_code()
    post_obj_fixture.check_type_name()
    post_obj_fixture.check_type_data()
    post_obj_fixture.check_type_id()


@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_create_object_negative(post_obj_fixture, data):
    post_obj_fixture.create_new_obj(data)
    post_obj_fixture.check_bad_request()
