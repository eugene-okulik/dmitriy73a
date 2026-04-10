from endpoints.endpoint import Endpoint
import requests
import allure


class PatchObj(Endpoint):
    @allure.step("Make changes in obj, method patch")
    def make_changes_in_obj(self, body=None):
        body = body if body else {'name': 'test888'}
        self.response = requests.patch(url=f"{self.url}/{self.js['id']}", json=body)
        self.js = self.response.json() if self.response.status_code == 200 else self.js
        return self.response

    @allure.step("Check correct name changes in obj, method patch")
    def check_correct_name(self):
        assert self.js["name"] == "test888", "поле name содержит не те данные что отправили"

    @allure.step("Check correct data changes in obj, method patch")
    def check_correct_data(self):
        assert self.js["data"] == {'color': 'qqq', 'size': 'zxc'}, \
            "в поле data изменились данные"
