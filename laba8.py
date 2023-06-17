import datetime

def log(func):
    def wrapper(*args, **kwargs):
        print("Время запуска функции:", datetime.datetime.now())
        print("Введенные параметры:", args)
        result = func(*args, **kwargs)
        print("Результат вычисления:", result)
        return result
    return wrapper

@log
def taxi_cost(distance_km):
    cost = float(round((((distance_km*1000)/140)*0.25)+4, 2))
    return cost

distance = 10 # пример расстояния в километрах
total_cost = taxi_cost(distance)
print("Итоговая сумма оплаты такси:", total_cost)