def test_delete_obj_positive(delete_obj_fixture):
    delete_obj_fixture.create_new_obj()
    delete_obj_fixture.delete_obj()
    delete_obj_fixture.delete_obj_status()


def test_delete_obj_text(delete_obj_fixture):
    delete_obj_fixture.create_new_obj()
    delete_obj_fixture.delete_obj()
    delete_obj_fixture.delete_obj_text()
