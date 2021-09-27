tickets_quantity = int(input("Введите количество билетов, которые вы хотите приобрести на мероприятие: "))
tickets_costs = []

for i in range(1, tickets_quantity + 1):
    age = int(input("Возраст посетителя под номером %d: " % i))
    if age >= 25:
        tickets_costs.append(1390)
    elif age >= 18:
        tickets_costs.append(990)
    else:
        tickets_costs.append(0)
    print(tickets_costs)
    print(type(tickets_quantity))

cost_summ = sum(tickets_costs)

if tickets_quantity > 3:
    cost_summ = int(cost_summ * 0.9)

print("Cумма к оплате = ", cost_summ, "рублей")