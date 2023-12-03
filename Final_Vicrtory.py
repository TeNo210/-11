from victory import victory_game
print('Добро пожаловать в игру Виторина')
name = input('Как тебя зовут?:')

print('Отлично!', name)
answer = input('И так ты готов?:')

if answer == 'Да':
    victory_game()
elif answer == 'Нет':
    print(('Не давай готовься тогда'))
else:
    print('Не могу понять, что ты хочешь от меня)')