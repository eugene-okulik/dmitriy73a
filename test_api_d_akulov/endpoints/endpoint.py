import allure
import requests


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    body_in_obj = {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'}
    response = None
    js = None
    del_obj = None

    @allure.step("Create new obj")
    def create_new_obj(self, body=None):
        body = body if body else self.body_in_obj
        self.response = requests.post(url=self.url, json=body)
        self.js = self.response.json() if self.response.status_code == 200 else None
        return self.response

    @allure.step("Delete obj")
    def delete_obj(self):
        self.del_obj = requests.delete(f"http://objapi.course.qa-practice.com/object/{self.js['id']}")

    @allure.step("Check status code 200")
    def check_response_status_code(self):
        assert self.response.status_code == 200, "неверный статус код, ожидали 200"

    @allure.step("Check that 400 error received")
    def check_bad_request(self):
        assert self.response.status_code == 400, "неверный статус код, ожидали 400"

    @allure.step("Check type name")
    def check_type_name(self):
        assert type(self.js["name"]) == str, "поле name содержит не str"

    @allure.step("Check type data")
    def check_type_data(self):
        assert type(self.js["data"]) == dict, "поле data содержит не dict"

    @allure.step("Check type id")
    def check_type_id(self):
        assert type(self.js["id"]) == int, "поле id содержит не int"
