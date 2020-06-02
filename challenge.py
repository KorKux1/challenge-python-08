import time
from datetime import datetime



def finish_date(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        timestamp = time.time()
        date = datetime.fromtimestamp(timestamp)
        date_format = date.strftime("%d/%m/%Y - %H:%M:%S")
        print(f'The function {func.__name__} ended at {date_format}')
    return wrapper

@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
