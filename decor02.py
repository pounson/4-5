from decorr import decorator_loger

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

@decorator_loger
def flat_generator(nested_list):
  for ln in nested_list:
    for i in ln:
      yield i

flat_list = []


for item in flat_generator(nested_list):
  flat_list.append(item)

print(flat_list)
