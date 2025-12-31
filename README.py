# A.-Two-Vessels
for _ in range(int(input())):
	a, b, c = map(int, input().split())
	_max = max(a, b)
	_min = min(a, b)
	count = 0
	while _max > _min:
		_max -= c
		_min += c
		count += 1
	print(count)
