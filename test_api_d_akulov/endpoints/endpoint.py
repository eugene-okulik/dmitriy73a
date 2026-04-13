import allure
import requests


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    body_in_obj = {'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'}
    response = None
    js = None
    del_obj = None

    @allure.step("Check status code 200")
    def check_response_status_code(self):
        assert self.response.status_code == 200, "неверный статус код, ожидали 200"

    @allure.step("Check that 400 error received")
    def check_bad_request(self):
        assert self.response.status_code == 400, "неверный статус код, ожидали 400"

    @allure.step("Check type name")
    def check_type_name(self):
        assert isinstance(self.js["name"], str), "поле name содержит не str"

    @allure.step("Check type data")
    def check_type_data(self):
        assert isinstance(self.js["data"], dict), "поле data содержит не dict"

    @allure.step("Check type id")
    def check_type_id(self):
        assert isinstance(self.js["id"], int), "поле id содержит не int"
