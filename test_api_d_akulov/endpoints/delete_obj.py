from endpoints.endpoint import Endpoint
import requests
import allure


class DeleteObj(Endpoint):

    @allure.step("Delete obj")
    def delete_obj(self, json_item_id):
        self.del_obj = requests.delete(f"http://objapi.course.qa-practice.com/object/{json_item_id}")

    @allure.step("Check correct status code delete obj")
    def delete_obj_status(self):
        assert self.del_obj.status_code == 200, "неверный статус код"

    @allure.step("Check correct text delete obj")
    def delete_obj_text(self, json_item_id):
        assert self.del_obj.text == f"Object with id {json_item_id} successfully deleted"
