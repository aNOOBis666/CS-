import requests
import datetime as dt
from statistics import median
from typing import Optional
from api import get_friends


def age_predict(user_id: int) -> Optional[float]:
	""" Наивный прогноз возраста по возрасту друзей
	Возраст считается как медиана среди возраста всех друзей пользователя
	:param user_id: идентификатор пользователя
	:return: медианный возраст пользователя
	"""
	assert isinstance(user_id, int), "user_id must be positive integer"
	assert user_id > 0, "user_id must be positive integer"

	friends_lst = get_friends(user_id, 'bdate')
	date_now = dt.datetime.now()
	year_now = date_now.year
	ages = []
	for person in friends_lst:
		try:
			date = person['bdate']
			date = dt.datetime.strptime(date, "%d.%m.%Y")
			ages.append(year_now - date.year)
		except:
			pass
	if not ages:
		return None
	else:
		return median(ages)


if __name__ == '__main__':
	age_inp = int(input('Введите нужный id: '))
	print(age_predict(age_inp))

	
	
