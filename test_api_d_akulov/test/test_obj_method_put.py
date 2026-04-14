import pytest

NEGATIVE_DATA = [{'name': 'test2'},
                 {'data': {'color': 'qqq', 'size': 'zxc'}},
                 {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 123}]


def test_put_obj_positive(put_obj_fixture, create_obj_fixture_id):
    put_obj_fixture.make_changes_in_obj(create_obj_fixture_id)
    put_obj_fixture.check_response_status_code()
    put_obj_fixture.check_type_name()
    put_obj_fixture.check_type_data()
    put_obj_fixture.check_type_id()
    put_obj_fixture.check_correct_name()
    put_obj_fixture.check_correct_data()


@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_put_obj_negative(put_obj_fixture, create_obj_fixture_id, data):
    put_obj_fixture.make_changes_in_obj(create_obj_fixture_id, data)
    put_obj_fixture.check_bad_request()
