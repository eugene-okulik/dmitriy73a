def test_patch_obj_status_code_check_type_data_id_name_check_correct_name_data(patch_obj_fixture,
                                                                               create_obj_fixture_id):
    patch_obj_fixture.make_changes_in_obj(create_obj_fixture_id)
    patch_obj_fixture.check_response_status_code()
    patch_obj_fixture.check_type_data()
    patch_obj_fixture.check_type_id()
    patch_obj_fixture.check_type_name()
    patch_obj_fixture.check_correct_name()
    patch_obj_fixture.check_correct_data()
