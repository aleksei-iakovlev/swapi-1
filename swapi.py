import requests
from pathlib import Path


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, base_url):
        try:
            response = requests.get(base_url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return f'Ошибка {e}'


class SWRequester(APIRequester):

    base_url = 'https://swapi.dev/api/'

    def __init__(self, base_url):

        super().__init__(base_url)

    def get_sw_categories(self, base_url):

        response = APIRequester(base_url)
        data = response.get(base_url)
        return data.keys()

    def get_sw_info(self, category):

        response = APIRequester(self.base_url)
        data = response.get(self.base_url + category)
        return str(data)

    def save_sw_data(self):
        object_sw_requester = SWRequester(self.base_url)
        Path('data').mkdir(parents=True, exist_ok=True)
        list_of_categories = object_sw_requester.get_sw_categories()
        for category in list_of_categories:
            with open(f'data/{category}.txt', 'w', encoding='utf-8') as f:
                file = self.get_sw_info(category)
                f.write(file)


# sw_check = SWRequester('https://swapi.py4e.com/api/')
# sw_check.save_sw_data()
# print(sw_check.get_sw_categories('https://swapi.dev/api/'))
