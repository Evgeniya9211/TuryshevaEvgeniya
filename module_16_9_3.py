class Client:
    def __init__(self, name="", surname="", balance=0):
        self.name = name
        self.surname = surname
        self.balance = balance

    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.surname = cat_dict.get("surname")
        self.balance = cat_dict.get("balance")

    def prnt_attribute(self, figure_dict):
        print('Клиент \"{data[name]} {data[surname]}\". Баланс: {data[balance]} руб.'.format(data=figure_dict))


clients = [{"name": "Иван", "surname": "Петров", "balance": 50},
              {"name": "Максим", "surname": "Васильевич",  "balance": 20},
              {"name": "Иосиф", "surname": "Сергеевич",  "balance": 70}]

for client in clients:
    volunteer_obj = Client()
    volunteer_obj.init_from_dict(client)
    volunteer_obj.prnt_attribute(client)
