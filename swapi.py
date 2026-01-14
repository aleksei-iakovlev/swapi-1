import requests
from pathlib import Path


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path):
        base = self.base_url.rstrip('/')
        endpoint = path.lstrip('/')
        url = base + '/' + endpoint
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):

    def __init__(self, base_url):

        super().__init__(base_url)

    def get_sw_categories(self):

        data = requests.get(f'{self.base_url}/')
        data = data.json()
        return data.keys()

    def get_sw_info(self, category):

        response = self.get(f'{category}/')
        return response.text


def save_sw_data():
    try:
        sw_requester = SWRequester('https://swapi.dev/api')

        Path('data').mkdir(exist_ok=True)
        list_of_categories = sw_requester.get_sw_categories()
        for category in list_of_categories:
            with open(f'data/{category}.txt', 'w', encoding='utf-8') as f:
                file = sw_requester.get_sw_info(category)
                f.write(file)
    except requests.exceptions.RequestException:
        print('Возникла ошибка при выполнении запроса')
# url for access https://swapi.py4e.com/api
# url for pytest https://swapi.dev/api


save_sw_data()
