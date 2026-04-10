from endpoints.endpoint import Endpoint
import requests
import allure


class DeleteObj(Endpoint):

    @allure.step("Check correct status code delete obj")
    def delete_obj_status(self):
        assert self.del_obj.status_code == 200, "неверный статус код"

    @allure.step("Check correct text delete obj")
    def delete_obj_text(self):
        id_del = self.js['id']
        assert self.del_obj.text == f"Object with id {id_del} successfully deleted"
