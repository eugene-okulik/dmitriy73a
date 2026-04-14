from endpoints.endpoint import Endpoint
import requests
import allure


class PutObj(Endpoint):

    @allure.step("Make changes in obj, method put")
    def make_changes_in_obj(self, id_item, body=None):
        body = body if body else {'data': {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'},
                                  'name': 'test777'}
        self.response = requests.put(url=f"{self.url}/{id_item}", json=body)
        # для себя, тут важно для негативных тестов что бы сохранился self.js изначальный, иначе не удалялся объект
        # так как нужен id объекта. Понимаю криво, но работает))
        self.js = self.response.json() if self.response.status_code == 200 else self.js
        return self.response

    @allure.step("Check correct name changes in obj, method put")
    def check_correct_name(self):
        assert self.js["name"] == "test777", "поле name содержит не те данные что отправили"

    @allure.step("Check correct data changes in obj, method put")
    def check_correct_data(self):
        assert self.js["data"] == {'color': 'test i am', 'size': 'big', 'еще что то': 'qwerty'}, \
            "поле data содержит не те данные что отправили"
