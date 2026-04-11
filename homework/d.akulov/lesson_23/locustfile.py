from locust import task, HttpUser


class ObjApi(HttpUser):
    id_obj = None

    # предусловие
    def on_start(self) -> None:
        response = self.client.post("/object", json={'data': {'color': 'qqq', 'size': 'zxc'}, 'name': 'test666'})
        self.id_obj = response.json()["id"]

    @task(1)
    def get_all_obj(self):
        self.client.get(f"/object")

    @task(3)
    def get_one_obj(self):
        self.client.get(f"/object/{self.id_obj}")

    # постусловие
    def on_stop(self):
        if self.id_obj:
            self.client.delete(f"/object/{self.id_obj}")
