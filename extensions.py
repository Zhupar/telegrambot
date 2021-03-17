import requests
import json

import config


class APIException(Exception):
    pass

class Convert:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise APIException('Неправильное количество параметров')
        quote, base, amount = values

        if quote not in config.KEYS.keys() or base not in config.KEYS.keys():
            raise APIException('Пожалуйста, выберите валюты из списка </values>')

        if base == quote:
            raise APIException('Невозможно перевести одинаковые валюты')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество <{amount}>')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={config.KEYS[quote]}&symbols={config.KEYS[base]}')
        r_content = json.loads(r.content)
        total_base = r_content['rates'][config.KEYS[base]]*float(amount)
        text = f'{amount} {quote} = {total_base} {base}'
        return text
