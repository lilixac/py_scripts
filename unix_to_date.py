OFFSET19700101 = 2440588
SECONDS_PER_DAY = 24 * 60 * 60

def _daysToDate(_days: int):
	'''
	Returns year, month and day based on the `_days` parameter.
	
	:param _days: It is equal to the unix timestamp / seconds_per_day.
	'''
	L = int(_days + 68569 + OFFSET19700101)
	N = int(4 * L // 146097)
	L = int(L - (146097 * N + 3) // 4)
	_year = int(4000 * (L + 1) // 1461001)
	L = int(L - 1461 * _year // 4 + 31)
	_month = int(80 * L // 2447)
	_day = int(L - 2447 * _month // 80)
	L = _month // 11;
	_month = _month + 2 - 12 * L
	_year = 100 * (N - 49) + _year + L

	year = int(_year);
	month = int(_month);
	day = int(_day);

	return year, month, day

def timeStampToDate( timestamp: int):
	'''
	:param timestamp: The timestamp of which we need year, month and day. 
	'''
	(year, month, day) = _daysToDate(timestamp / SECONDS_PER_DAY)
	return year, month, day

a = input("Enter timestamp: ")

print(timeStampToDate(int(a)))
