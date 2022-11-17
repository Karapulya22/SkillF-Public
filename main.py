ticket_needs = int(input('Введите количество билетов'))
no_money = 0
money = 0
money_pay = 0
for i in range(ticket_needs):
    age = int(input('Возраст='))
    if age < 18:
        money += 0
        no_money += 1
        print('бесплатный билет')
    elif 18 <= age < 25:
        money += 990
        money_pay += 1
        print('цена билета=990 рублей')
    else:
        money += 1390
        money_pay += 1
        print('цена билета=1390 рублей')

if ticket_needs > 3 and money >3690:
    print('цена билетов всего =', money)
    print(f'скидка 10%, так как оплата за {money_pay} посетителей ')
    money = money - ((money / 100)*10)

print(f'Итого: {money} рублей')
print(f'Бесплатно- {no_money} посетителей')