def test_delete_obj_status_code_and_text(delete_obj_fixture, create_obj_fixture_id):
    delete_obj_fixture.delete_obj(create_obj_fixture_id)
    delete_obj_fixture.delete_obj_status()
    delete_obj_fixture.delete_obj_text(create_obj_fixture_id)
