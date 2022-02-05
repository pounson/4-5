import datetime

FILE_PATH = 'parametrized_decoratorlogs.txt'

def parametrized_decor(parameter):
  def decorator_loger(old_function):
    def new_function(*args, **kwargs):
      date_time = datetime.datetime.now()
      name_function = old_function.__name__
      result = old_function(*args, **kwargs)
      with open(parameter, 'w') as file:
        file.write( f'Дата/время: {date_time}\n'
                    f'Имя функции: {name_function}\n'
                    f'Аргументы: {args, kwargs}\n'
                    f'Результат: {result}\n')
      return result
    return new_function
  return decorator_loger

if __name__ == "__main__":
  @parametrized_decor(FILE_PATH)
  def summ(a, b):
    return a - b

  summ(6, 2)
