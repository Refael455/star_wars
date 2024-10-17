""" Tries to get info for Luke Skywalker"""  # ඞ
import requests
import urljoin


URL = "https://swapi.dev/api/"

INFO_LINK = "/people/"


def people_get(number):
    """get data and return some values"""
    response = requests.get(
        urljoin.url_path_join(URL, INFO_LINK, str(number)),
        timeout=15
    )
    if response.status_code != 200:
        raise ValueError(response.status_code)
    data = response.json()
    return {
        'name': data['name'],
        'gender': data['gender'],
        'born': data['birth_year']
    }


if __name__ == "__main__":
    for i in range(1, 5):
        print(i, people_get(i))