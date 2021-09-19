per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму, которую планируете положить под проценты: ")
money_int = int(money)
list_per_cent = per_cent.values()
deposit = list(map(lambda x: round(x / 100 * money_int), list_per_cent))
deposit_int = list(map(int, deposit))
print("money = ", money_int)
print("deposit = ", deposit_int)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit_int))