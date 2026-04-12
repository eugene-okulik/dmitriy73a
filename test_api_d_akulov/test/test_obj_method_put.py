import pytest

NEGATIVE_DATA = [{'name': 'test1'},
                 {'data': {'color': 'qqq', 'size': 'zxc'}},
                 {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 123}]


def test_put_obj_positive(put_obj_fixture):
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_response_status_code()


@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_put_obj_negative(put_obj_fixture, data):
    put_obj_fixture.make_changes_in_obj(data)
    put_obj_fixture.check_bad_request()


def test_check_type_name_date_id_check_correct_name_date(put_obj_fixture):
    put_obj_fixture.make_changes_in_obj()
    put_obj_fixture.check_type_name()
    put_obj_fixture.check_type_data()
    put_obj_fixture.check_type_id()
    put_obj_fixture.check_correct_name()
    put_obj_fixture.check_correct_data()
