def test_put_obj_positive(patch_obj_fixture):
    patch_obj_fixture.create_new_obj()
    patch_obj_fixture.make_changes_in_obj()
    patch_obj_fixture.check_response_status_code()
    patch_obj_fixture.delete_obj()


def test_check_type_name(patch_obj_fixture):
    patch_obj_fixture.create_new_obj()
    patch_obj_fixture.make_changes_in_obj()
    patch_obj_fixture.check_type_name()
    patch_obj_fixture.delete_obj()


def test_check_type_data(patch_obj_fixture):
    patch_obj_fixture.create_new_obj()
    patch_obj_fixture.make_changes_in_obj()
    patch_obj_fixture.check_type_data()
    patch_obj_fixture.delete_obj()


def test_check_type_id(patch_obj_fixture):
    patch_obj_fixture.create_new_obj()
    patch_obj_fixture.make_changes_in_obj()
    patch_obj_fixture.check_type_id()
    patch_obj_fixture.delete_obj()


def test_check_correct_name(patch_obj_fixture):
    patch_obj_fixture.create_new_obj()
    patch_obj_fixture.make_changes_in_obj()
    patch_obj_fixture.check_correct_name()
    patch_obj_fixture.delete_obj()


def test_check_correct_data(patch_obj_fixture):
    patch_obj_fixture.create_new_obj()
    patch_obj_fixture.make_changes_in_obj()
    patch_obj_fixture.check_correct_data()
    patch_obj_fixture.delete_obj()
