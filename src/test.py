import requests
import json


def main():
    url = 'http://localhost:8000'
    data = {
        'cost': 100,
        'tax_rate': 0.1
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == '__main__':
    main()
