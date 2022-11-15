import time
from change_day import change_date



def run():
    hola = time.localtime()
    day = time.asctime(hola)
    hi = change_date(day)
    print(hi)


if __name__ == '__main__':
    run()