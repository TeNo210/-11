    print('Добро пожаловать в игру Виторина')
    name = input('Как тебя зовут?:')

    print('Отлично!', name)
    answer = input('И так ты готов?:')

    if answer == 'Да':
        victory_game()
    elif answer == 'Нет':
        print(('Не давай готовься тогда)'))
    else:
        print('Не могу понять, что ты хочешь от меня)')
    import random
    def victory_game():

    FAMOUS_PEOPLE = {'Александр Сергееви Пушкин': '26.09.1799', 'М.И.Лермонтов': '15.10.1814',
                     'С.А.Есенин': '3.10.1895', 'В.С.Высоцкий': '25.01.1938',
                     'С.П.Королев': '12.01.1907', 'В.П.Глушко': '20.08.1908',
                     'A.Н.Туполев': '29.10.1888', 'Ю.А.Гагарин': '09.03.1934'}
    rounds = int(input('Сколько раз вы хотели играть?:'))
    for i in range(rounds):
        'name,date' - random.choice(list(FAMOUS_PEOPLE.items()))
        answer = input('Когда родился {name}')
        if answer == 'date':
            print('Верно')
        else:
            print('Неверно')
    print('Пока')
victory_game()