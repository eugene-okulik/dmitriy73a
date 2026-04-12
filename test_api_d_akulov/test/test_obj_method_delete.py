def test_delete_obj_status_code_and_text(delete_obj_fixture):
    delete_obj_fixture.delete_obj()
    delete_obj_fixture.delete_obj_status()
    delete_obj_fixture.delete_obj_text()
