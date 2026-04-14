import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObj(Endpoint):

    @allure.step("Create new obj")
    def create_new_obj(self, body=None):
        body = body if body else self.body_in_obj
        self.response = requests.post(url=self.url, json=body)
        self.js = self.response.json() if self.response.status_code == 200 else None
        return self.response
