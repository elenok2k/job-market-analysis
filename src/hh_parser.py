import requests

url = "https://api.hh.ru/vacancies"

params = {
    "text": "Data Analyst",
    "per_page": 20
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

