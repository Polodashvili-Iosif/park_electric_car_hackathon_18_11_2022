import os
from base64 import b64decode
from pprint import pprint

import requests
from twocaptcha import TwoCaptcha


def get_car_data(vin: str) -> dict[str: str]:
    if vin:
        r = requests.get('https://check.gibdd.ru/captcha').json()

        file_name = 'captcha.png'
        with open(file_name, "wb") as f:
            f.write(b64decode(r["base64jpg"]))

        solver = TwoCaptcha('82cec7e414bf1e0e02dba52d4fcadab1')
        result = solver.normal(file_name)

        os.remove(file_name)

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://xn--90adear.xn--p1ai',
            'Referer': 'https://xn--90adear.xn--p1ai/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'vin': vin,
            'checkType': 'history',
            'captchaWord': result['code'],
            'captchaToken': r['token'],
        }

        response = requests.post('https://xn--b1afk4ade.xn--90adear.xn--p1ai/proxy/check/auto/history', headers=headers,
                                 data=data).json()['RequestResult']['vehicle']
        return response


if __name__ == '__main__':
    get_car_data('5YJ3E1EBXJF135746')
