import requests
import time

import config


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
<<<<<<< HEAD
	""" Выполнить GET-запрос
	:param url: адрес, на который необходимо выполнить запрос
	:param params: параметры запроса
	:param timeout: максимальное время ожидания ответа от сервера
	:param max_retries: максимальное число повторных запросов
	:param backoff_factor: коэффициент экспоненциального нарастания задержки
	"""
	delay = 0.1
	retries = 0
	while retries < max_retries:
		try:
			response = requests.get(url, params, str(timeout))
			response.raise_for_status()
			if response.status_code == 200:
				return response
		except requests.exceptions.RequestException:
			time.sleep(delay)
			delay = delay * backoff_factor + random.random()
			retries += 1
	return False
=======
    """ Выполнить GET-запрос
    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    delay = 0.1
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, params, str(timeout))
            response.raise_for_status()
            if response.status_code == 200:
                return response
        except requests.exceptions.RequestException:
            time.sleep(delay)
            delay = delay * backoff_factor + random.random()
            retries += 1
    return False
>>>>>>> fafe54a5c7ab0b14f1242a0a5eb453ea202020cb


def get_friends(user_id, fields):
	""" Вернуть данных о друзьях пользователя
	:param user_id: идентификатор пользователя, список друзей которого нужно получить
	:param fields: список полей, которые нужно получить для каждого пользователя
	"""
	assert isinstance(user_id, int), "user_id must be positive integer"
	assert isinstance(fields, str), "fields must be string"
	assert user_id > 0, "user_id must be positive integer"
	domain = "https://api.vk.com/method"
	access_token = '495c047d89dba607e183dbd5730fcd6eb4297ef5b6d47871cfc78e97fd07208435e64c9eea2fe63cd21e3'
	user_id = user_id
	fields = fields
	v = '5.103'
	query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
	response = requests.get(query)
	r = response.json()
	return r['response']['items']
